from .db_conn import get_db_conn
from werkzeug.security import generate_password_hash

# Default password for admin
DEFAULT_ADMIN_PASS = generate_password_hash('admin')


def create_admin():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO USERS (username, password, isAdmin)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
                ''', ('dkulis', DEFAULT_ADMIN_PASS, True))

# Insert processed data into database


def insert():
    conn = get_db_conn()
    cur = conn.cursor()

    # Example insert (HARD CODED)
    cur.execute('''
                INSERT INTO GPUS (store, gpu, manufacturer, memory, price, link) 
                VALUES('Micro Center', 'GTX 3050', 'Asus', 8, 429.99, '')''')

    cur.close()
    conn.commit()
