def infer_severity(drug_a, drug_b):
    # Rule-based placeholder (extend later)
    high_risk_drugs = {"warfarin", "fentanyl", "clozapine"}

    if drug_a in high_risk_drugs or drug_b in high_risk_drugs:
        return "high"
    return "unknown"
