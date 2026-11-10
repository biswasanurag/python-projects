import sys
from parkfinder import load_parks, show_results, format_detail

def filter_by_state(parks, state):
    matches = []
    for park in parks:
        for park_state in park["states"]:
            if park_state.lower() == state.lower():
                matches.append(park)
    return matches

def filter_by_activity(parks, activity):
    matches = []
    for park in parks:
        if activity.lower() in park["activities"]:
            matches.append(park)
    return matches


if len(sys.argv) < 2:
    print("Usage: python browse.py <state> [activity]")
    sys.exit()

state = sys.argv[1]

parks = load_parks()
matches = filter_by_state(parks, state)
if len(sys.argv) > 2:
    activity = sys.argv[2]
    matches = filter_by_activity(matches, activity)
show_results(matches, False)

if matches:
    with open("results.txt", "w") as file:
        for park in matches:
            details = format_detail(park)
            file.write(details)
            file.write("\n\n")

    print(f"\nWrote {len(matches)} park(s) to results.txt")