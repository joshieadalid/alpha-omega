import sqlite3


# Function to connect to the database
def connect():
    return sqlite3.connect('my_database.db')


# Function to create tables (run only once at the start)
def create_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        permissions TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS minutes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
    ''')
    conn.commit()
    conn.close()
    print("Tables created or verified successfully.")
