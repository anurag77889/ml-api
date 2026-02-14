import sqlite3

# Create SQLite database connection
conn = sqlite3.connect("predictions.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        salary REAL,
        prediction INTEGER   
   )
""")
conn.commit()

def insert_prediction(age, salary, prediction):
    # Insert into DB
        cursor.execute(
            "INSERT INTO predictions (age, salary, prediction) VALUES (?, ?, ?)",
            (age, salary, int(prediction))
        )
        conn.commit()
