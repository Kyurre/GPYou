from werkzeug.security import generate_password_hash
# import os
# import sys

# directory reach
# current = os.path.dirname(os.path.realpath(__file__))

# setting path
# parent = os.path.dirname(current)

# Through parent website/<file> 
# sys.path.append(parent)
from .parser import createAmazonTuple

#Current directly
# add a '.' to front of db_conn and tables when running from wsgi and remove it when running file independently
from .db_conn import get_db_conn #add a '.' 
from .db_tables import drop_gpu_table, create_tables #add a '.' 


# Default password for admin
DEFAULT_ADMIN_PASS = generate_password_hash('admin')


def create_admin():
    """create default admin"""

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO USERS (username, password, isAdmin)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
                ''', ('dkulis', DEFAULT_ADMIN_PASS, True))


def insert_to_db():
    """insert processed data into database"""

    conn = get_db_conn()
    cur = conn.cursor()

    # Insert statement
    #  TODO: Fix issue with empty '' insert into SMALL INT 
    insert_smt = (
        "INSERT INTO GPUS (store, gpu, manufacturer, memory, price, link)" 
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    
    # Data
    amazon_gpu_list = createAmazonTuple()
    
    for i in range(0, len(amazon_gpu_list)):
        cur.execute(insert_smt, amazon_gpu_list[i])

    cur.close()
    conn.commit()



# create_tables()
# insert_to_db()

