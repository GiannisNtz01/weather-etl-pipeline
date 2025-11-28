import json
import pandas as pd
import glob
from datetime import datetime, timedelta

def transform_weather():
    # Βρίσκουμε το πιο πρόσφατο raw JSON αρχείο
    json_files = sorted(glob.glob("raw_weather_*.json"))
    if not json_files:
        print("No raw JSON files found.")
        return

    latest_file = json_files[-1]
    print(f"[INFO] Transforming: {latest_file}")

    # Διαβάζουμε το JSON
    with open(latest_file, "r") as f:
        data = json.load(f)

    times = pd.to_datetime(data["hourly"]["time"])
    temps = data["hourly"]["temperature_2m"]

    df = pd.DataFrame({
        "timestamp": times,
        "temperature": temps
    })

    # Φιλτράρουμε τις επόμενες 48 ώρες
    now = pd.Timestamp.now()
    df = df[(df["timestamp"] >= now) & (df["timestamp"] <= now + pd.Timedelta(hours=48))]

    # Αποθήκευση σε CSV
    csv_filename = latest_file.replace(".json", "_next48h.csv")
    df.to_csv(csv_filename, index=False)
    print(f"[OK] Transformed CSV for next 48h saved as {csv_filename}")

if __name__ == "__main__":
    transform_weather()
