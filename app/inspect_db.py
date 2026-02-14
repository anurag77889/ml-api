import sqlite3

# Create SQLite database connection
conn = sqlite3.connect("predictions.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("SELECT age, salary, prediction FROM predictions")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()