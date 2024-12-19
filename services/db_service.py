import sqlite3

DATABASE = 'app.db'

def get_db():
    """Conexión a la base de datos."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Acceso a columnas por nombre
    return conn

def close_database_connection(exception=None):
    """Cierra la conexión a la base de datos."""
    conn = getattr(exception, '_database', None)
    if conn is not None:
        conn.close()

def init_db():
    """Inicializa la base de datos con un esquema."""
    conn = get_db()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
