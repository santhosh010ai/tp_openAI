# Directory: travel_planner/main.py

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from agent.graph import build_travel_agent
from agent.state import AgentState

def main():
    if not openai_api_key:
        raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")
        
    graph = build_travel_agent()
    initial_state = AgentState(history=[{"user": "I want a cultural and food trip for 5 days with a medium budget."}])
    final_state = graph.invoke(initial_state)
    print(final_state)

if __name__ == "__main__":
    main()
