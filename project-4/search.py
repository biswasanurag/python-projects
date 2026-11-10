import json, sys
from parkfinder import load_parks, show_results


def find_matches(parks, search):
    matches = []
    for park in parks:
        if search.lower() in park["name"].lower():
            matches.append(park)
    return matches

if len(sys.argv) < 2:
    print("Usage: python search.py <search term>")
    sys.exit()

parks = load_parks()
search = sys.argv[1]
detail = "detail" in sys.argv

matches = find_matches(parks, search)
show_results(matches, detail)