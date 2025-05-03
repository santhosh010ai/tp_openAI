from ..tools.destination_db import get_destinations
from agent.state import AgentState

def find_destinations(state: AgentState):
    state.destinations = get_destinations(state.preferences)
    return state