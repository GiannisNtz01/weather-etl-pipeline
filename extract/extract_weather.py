import requests
import json
from datetime import datetime

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=37.9838&longitude=23.7275&hourly=temperature_2m"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # θα εμφανίσει error αν δεν 200
        data = response.json()

        filename = f"raw_weather_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[OK] Weather data saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch data: {e}")

if __name__ == "__main__":
    fetch_weather()
