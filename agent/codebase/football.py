import requests

# Function to fetch data from the API
def get_standings(league_id, api_key):
    url = f"https://api.football-data.org/v4/competitions/{league_id}/standings"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["standings"][0]["table"]
    else:
        return None

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'KEY HERE'

# Premier League ID in football-data.org API
premier_league_id = 'PL'

# Fetch standings
standings = get_standings(premier_league_id, API_KEY)

if standings:
    # Sort teams by position
    sorted_teams = sorted(standings, key=lambda x: x["position"])

    # Print table header
    print("{:<5} {:<25} {:<10}".format(
        "Pos", "Team", "Points"
    ))
    print("-" * 40)

    # Print each team and their points
    for team in sorted_teams:
        team_name = team["team"]["name"]
        total_points = team["points"]

        print("{:<5} {:<25} {:<10}".format(
            team["position"], team_name, total_points
        ))
else:
    print("Failed to fetch standings.")
