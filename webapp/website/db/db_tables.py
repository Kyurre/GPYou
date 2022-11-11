from .db_conn import get_db_conn


def create_tables():
    conn = get_db_conn()
    cur = conn.cursor()

    # Dave: I think we should remove this drop because it's resetting the users table everytime
    cur.execute('DROP TABLE IF EXISTS GPUS CASCADE')
    # cur.execute("DROP TABLE IF EXISTS USERS CASCADE;")  # ls nov 6 EC2REMOVE
    cur.execute("DROP TABLE IF EXISTS FAVORITES CASCADE;")  # Remove for EC2

    # create users table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS USERS (
                    user_id     SERIAL UNIQUE PRIMARY KEY,
                    username    VARCHAR(32) NOT NULL UNIQUE,
                    password    VARCHAR(255) NOT NULL,
                    isAdmin     BOOL DEFAULT FALSE
                )
                ''')
    # create gpu table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS GPUS (
                    gpu_id          SERIAL UNIQUE PRIMARY KEY,
                    store           TEXT,
                    gpu             TEXT,
                    manufacturer    TEXT,
                    memory          SMALLINT,
                    price           FLOAT,
                    link            TEXT
                )
                ''')
    # create favorites table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS FAVORITES (
                    gpuid                   INTEGER,
                    username                INTEGER,
                    CONSTRAINT fk_gpu       FOREIGN KEY (gpuid) REFERENCES GPUS(gpu_id),
                    CONSTRAINT fk_username  FOREIGN KEY (username) REFERENCES USERS(user_id)
                )
                ''')

    cur.close()
    conn.commit()
