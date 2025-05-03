from typing import Dict, List, Any
from pydantic import BaseModel

class AgentState(BaseModel):
    preferences: Dict[str, Any] = {}
    destinations: List[Dict[str, Any]] = []
    itinerary: Dict[str, Any] = {}
    history: List[Dict[str, str]] = []
    is_followup: bool = False