import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Σύνδεση στη βάση SQLite
conn = sqlite3.connect("weather.db")
df = pd.read_sql_query("SELECT * FROM weather ORDER BY timestamp", conn)
conn.close()

# Μετατροπή timestamp σε datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Επιλογή **επόμενων 48 ωρών** από την τρέχουσα στιγμή
now = pd.Timestamp.now()
df = df[df['timestamp'] >= now].head(48)

# Δημιουργία plot
plt.figure(figsize=(14,6))
plt.plot(df['timestamp'], df['temperature'], marker='o', color='tab:blue')
plt.title("Next 48 Hours Temperature Forecast in Athens", fontsize=16)
plt.xlabel("Time (Date & Hour)", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True)

# Format άξονα Χ
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))

# Major ticks κάθε 6 ώρες
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))

plt.xticks(rotation=60)
plt.tight_layout()
plt.show()
