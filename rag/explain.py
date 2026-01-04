from rag.retrieve import retrieve_interaction_text

def explain_interaction(drug_a, drug_b):
    context_chunks = retrieve_interaction_text(drug_a, drug_b)

    if not context_chunks:
        return "Insufficient data to explain this interaction."

    explanation = f"""
    Known interaction detected between {drug_a} and {drug_b}.

    Evidence:
    {context_chunks[0]}

    Clinical Risk:
    This interaction has been reported in curated drug–drug interaction databases.
    Further clinical evaluation is recommended.

    Disclaimer:
    This is not medical advice.
    """

    return explanation.strip()
