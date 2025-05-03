import json
import os

def get_destinations(preferences):
    with open(os.path.join("data", "destinations.json"), "r") as f:
        all_destinations = json.load(f)

    results = []
    for dest in all_destinations:
        if preferences["budget"] == dest["budget_level"] and \
           any(tag in dest["tags"] for tag in preferences["interests"]):
            results.append(dest)
    return results