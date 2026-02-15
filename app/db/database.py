import sqlite3

# Create SQLite database connection
def get_db_connection():
    conn = sqlite3.connect("predictions.db")
    return conn 

# Create the PREDICTIONS table
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()      

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            salary REAL,
            prediction INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
        )
    """)
    conn.commit()
    conn.close()

# Add PREDICTIONS into the database
def insert_prediction(age, salary, prediction):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Insert into DB
    cursor.execute(
        "INSERT INTO predictions (age, salary, prediction) VALUES (?, ?, ?)",
        (age, salary, int(prediction))
    )
    conn.commit()
    conn.close()


# Get recent PREDICTIONS
def get_recent_predictions(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT age, salary, prediction, created_at FROM predictions ORDER BY DESC LIMIT ?", (limit, ))

    rows = cursor.fetchall()
    conn.close()

    return rows 