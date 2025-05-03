from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_followup(state):
    last_question = state.history[-1]['user']
    prompt = f"Answer this follow-up question in context of the trip: {last_question}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    state.history.append({"agent": response.choices[0].message.content})
    return state