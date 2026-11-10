import json

def load_parks():
    with open("parks.json", "r") as file:
        return json.load(file)

def format_detail(park):
    return f"""{park["full_name"]}
    Description: {park["description"]}
    State(s): {", ".join(park["states"])}
    Entrance fee: ${park["entrance_fee"]}
    Best Seasons: {", ".join(park["best_seasons"])}
    Activities: {", ".join(park["activities"])}"""

def show_results(matches, detail):
    if not matches:
        print("No parks found.")
        return
    print(f"{len(matches)} park(s) found:")
    for park in matches:
        if detail:
            print()
            print(format_detail(park))
        else:
            states = ", ".join(park["states"])
            print(f"{park["name"]} - {states} (${park["entrance_fee"]})")