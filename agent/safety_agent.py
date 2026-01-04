import os
import logging
import google.generativeai as genai

from graph.queries import get_interaction
from rag.retrieve import retrieve_interaction_text
from agent.schema import InteractionResult

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

EXPLANATION_PROMPT = """
You are a medical explanation assistant.

Rewrite the VERIFIED FACTS below into simple,
human-readable language.

Rules:
- Do NOT add new medical facts
- Do NOT guess severity or mechanism
- Do NOT give medical advice
- If evidence is missing, state that clearly

VERIFIED FACTS:
{facts}
"""

def safety_agent(drug_a: str, drug_b: str) -> InteractionResult:
    interaction = get_interaction(drug_a, drug_b)

    interaction_exists = interaction is not None
    severity = "unknown"

    evidence = retrieve_interaction_text(drug_a, drug_b)

    facts = {
        "drug_pair": [drug_a, drug_b],
        "interaction_exists": interaction_exists,
        "severity": severity,
        "evidence": evidence
    }

    try:
        response = model.generate_content(
            EXPLANATION_PROMPT.format(facts=facts)
        )
        explanation = response.text.strip()

    except Exception as e:
        logging.error(f"Gemini explanation failed: {e}")

        explanation = (
            f"{drug_a.capitalize()} and {drug_b.capitalize()} are known to interact "
            "according to curated drug–drug interaction databases. "
            "No detailed explanation was available at this time. "
            "This information is provided for educational purposes only and "
            "is not medical advice."
        )

    return InteractionResult(
        drug_pair=[drug_a, drug_b],
        interaction_exists=interaction_exists,
        severity=severity,
        explanation=explanation,
        source="DDInter + RAG",
        disclaimer="This information is for educational purposes only and is not medical advice."
    )
