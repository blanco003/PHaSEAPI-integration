from typing import Optional
from pydantic import BaseModel


class HealthinessInfo(BaseModel):
    score: str 
    qualitative: Optional[str] = None

class SustainabilityInfo(BaseModel):
    score: str  
    qualitative: Optional[str] = None
    CF: Optional[float] = None
    WF: Optional[float] = None