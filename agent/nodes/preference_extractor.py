from openai import OpenAI
from agent.state import AgentState
import os
#print("API KEY:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_preferences(state: AgentState):
    user_input = state.history[-1]['user']
    prompt = f"""
    Extract preferences (budget, duration in days, interests) from the following travel request:

    "{user_input}"

    Return it in JSON format with keys: budget, duration, interests (a list).
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a travel planner assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    import json
    preferences = json.loads(response.choices[0].message.content)
    state.preferences = preferences
    return state
