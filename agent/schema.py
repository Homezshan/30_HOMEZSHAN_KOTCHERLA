from pydantic import BaseModel
from typing import List, Optional

class InteractionResult(BaseModel):
    drug_pair: List[str]
    interaction_exists: bool
    severity: Optional[str]
    explanation: Optional[str]
    source: str
    disclaimer: str
