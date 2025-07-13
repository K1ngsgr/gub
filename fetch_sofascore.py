import requests

def fetch_live_tennis_matches():
    try:
        response = requests.get("https://api.sofascore.com/api/v1/sport/tennis/events/live")
        data = response.json()
        matches = []

        for event in data.get("events", []):
            match_name = event['tournament']['name']
            home = event['homeTeam']['name']
            away = event['awayTeam']['name']
            score = event.get('status', {}).get('description', 'Live')
            match_id = event.get('id')

            matches.append({
                'id': match_id,
                'match': f"{home} vs {away}",
                'tournament': match_name,
                'score': score
            })

        return matches
    except Exception as e:
        print("Error fetching matches:", e)
        return []
