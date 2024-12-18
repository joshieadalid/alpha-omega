from database import connect


def insert_user(name, email, permissions=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, email, permissions)
    VALUES (?, ?, ?)
    ''', (name, email, permissions))
    conn.commit()
    conn.close()
    print("User inserted successfully.")


def get_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
