import json
import pandas as pd
import glob

def transform_weather():
    # Βρίσκουμε το πιο πρόσφατο raw αρχείο JSON
    json_files = sorted(glob.glob("raw_weather_*.json"))
    if not json_files:
        print("No raw JSON files found.")
        return

    latest_file = json_files[-1]
    print(f"[INFO] Transforming: {latest_file}")

    # Διαβάζουμε το αρχείο
    with open(latest_file, "r") as f:
        data = json.load(f)

    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]

    # Φτιάχνουμε DataFrame
    df = pd.DataFrame({
        "timestamp": times,
        "temperature": temps
    })

    # Σώζουμε σε csv
    output_file = latest_file.replace(".json", ".csv")
    df.to_csv(output_file, index=False)

    print(f"[OK] Transformed CSV saved as {output_file}")


# Κλήση της συνάρτησης
if __name__ == "__main__":
    transform_weather()
