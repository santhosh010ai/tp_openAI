import unittest
import sys
import os

# Fix for ModuleNotFoundError when running with `python -m unittest`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.graph import build_travel_agent
from agent.state import AgentState

class TestTravelAgent(unittest.TestCase):

    def setUp(self):
        self.graph = build_travel_agent()

    def test_full_flow(self):
        state = AgentState(
            history=[{"user": "Plan a trip with culture and food for 5 days, medium budget."}],
            preferences={"duration": 5, "interests": ["culture", "food"], "budget": "medium"},
            destinations=[
                {"name": "Paris"}, {"name": "Rome"}, {"name": "Barcelona"},
                {"name": "Amsterdam"}, {"name": "Vienna"}, {"name": "Berlin"}
            ]
        )
        result = self.graph.invoke(state)
        self.assertIn("generated_by_llm", result["itinerary"])


if __name__ == "__main__":
    unittest.main()

