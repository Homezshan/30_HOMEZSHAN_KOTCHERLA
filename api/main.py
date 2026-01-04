from fastapi import FastAPI
from agent.safety_agent import safety_agent
from agent.schema import InteractionResult

app = FastAPI(
    title="PharmaVision AI",
    description="Graph + RAG powered Drug–Drug Interaction Safety Agent",
    version="1.0"
)

@app.get("/check-interaction", response_model=InteractionResult)
def check_interaction(drug_a: str, drug_b: str):
    """
    Check if two drugs interact and return a safety-aware explanation.
    """
    return safety_agent(drug_a, drug_b)
