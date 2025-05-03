import re
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_itinerary(state):
    # Ensure the value is an integer, handle cases like '5 days'
    duration_raw = state.preferences.get("duration", 5)
    if isinstance(duration_raw, str):
        match = re.search(r'\d+', duration_raw)  # Extract digits from a string like '5 days'
        duration = int(match.group()) if match else 5
    else:
        duration = int(duration_raw)

    destinations = state.destinations[:duration]

    prompt = f"""
    Create a travel itinerary for the following destinations over {duration} days.
    User interests: {', '.join(state.preferences['interests'])}.
    Destinations: {[d['name'] for d in destinations]}.
    Include weather forecast and 2 activities per day.
    """
    
    # Call OpenAI to generate the itinerary
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a travel planner bot."},
            {"role": "user", "content": prompt},
        ]
    )

    # Update the state with the generated itinerary
    state.itinerary = {"generated_by_llm": response.choices[0].message.content}
    return state
