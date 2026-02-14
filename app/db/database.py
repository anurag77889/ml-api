import sqlite3

# Create SQLite database connection
def get_db_connection():
    conn = sqlite3.connect("predictions.db")
    return conn 

def create_table():
    conn = get_db_connection()
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
    conn.close()

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