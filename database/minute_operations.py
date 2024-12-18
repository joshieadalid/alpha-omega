from database import connect


def insert_minute(content):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO minutes (content)
    VALUES (?)
    ''', (content,))
    conn.commit()
    conn.close()
    print("Minute inserted successfully.")


def get_minutes():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM minutes")
    minutes = cursor.fetchall()
    conn.close()
    return minutes
