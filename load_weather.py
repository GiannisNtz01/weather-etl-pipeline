import pandas as pd
import sqlite3
import glob

def load_weather():
    # βρίσκουμε το τελευταίο CSV
    csv_files = sorted(glob.glob("raw_weather_*.csv"))
    if not csv_files:
        print("No CSV files found.")
        return

    latest_csv = csv_files[-1]
    print(f"[INFO] Loading: {latest_csv}")

    df = pd.read_csv(latest_csv)

    # Συνδέουμε σε SQLite DB (δημιουργείται αν δεν υπάρχει)
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    # Δημιουργία πίνακα
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL
        )
    """)

    # Φόρτωση δεδομένων
    df.to_sql("weather", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    print("[OK] Data loaded into weather.db")

if __name__ == "__main__":
    load_weather()
