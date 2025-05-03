from langgraph.graph import StateGraph
from .state import AgentState
from .nodes.preference_extractor import extract_preferences
from .nodes.destination_finder import find_destinations
from .nodes.itinerary_creator import create_itinerary
from .nodes.followup_handler import handle_followup

def build_travel_agent():
    workflow = StateGraph(state_schema=AgentState)
    
    # Define the nodes
    workflow.add_node("extract_preferences", extract_preferences)
    workflow.add_node("find_destinations", find_destinations)
    workflow.add_node("create_itinerary", create_itinerary)
    workflow.add_node("handle_followup", handle_followup)
    
    # Add an 'END' node as a placeholder
    workflow.add_node("END", lambda state: None)  # END node does nothing

    # Add edges between nodes
    workflow.add_edge("extract_preferences", "find_destinations")
    workflow.add_edge("find_destinations", "create_itinerary")
    workflow.add_conditional_edges("create_itinerary", lambda state: "handle_followup" if state.is_followup else "END")
    workflow.add_edge("handle_followup", "END")  # Ensure "END" is part of the graph

    # Set entry point
    workflow.set_entry_point("extract_preferences")
    
    return workflow.compile()
