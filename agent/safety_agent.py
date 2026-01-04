from graph.queries import get_interaction
from rag.explain import explain_interaction
from agent.rules import infer_severity
from agent.schema import InteractionResult

DISCLAIMER = "This information is for educational purposes only and is not medical advice."

def safety_agent(drug_a, drug_b):
    drug_a = drug_a.lower().strip()
    drug_b = drug_b.lower().strip()

    # 1️⃣ Knowledge Graph Gate
    interaction = get_interaction(drug_a, drug_b)

    if not interaction:
        return InteractionResult(
            drug_pair=[drug_a, drug_b],
            interaction_exists=False,
            severity=None,
            explanation=None,
            source="DDInter Knowledge Graph",
            disclaimer=DISCLAIMER
        )

    # 2️⃣ Severity Rules
    severity = infer_severity(drug_a, drug_b)

    # 3️⃣ Explanation (Controlled)
    explanation = explain_interaction(drug_a, drug_b)

    return InteractionResult(
        drug_pair=[drug_a, drug_b],
        interaction_exists=True,
        severity=severity,
        explanation=explanation,
        source="DDInter + RAG",
        disclaimer=DISCLAIMER
    )
