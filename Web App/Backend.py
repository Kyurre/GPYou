import psycopg2             # python -> psql connection
import pandas as pd         # create dataframes 



conn = psycopg2.connect("dbname=test user=user_name")    #connect to an existing database
cur = conn.cursor()     #cursor for database operations

#Once Connection is established


# Our Data:

addr_df=pd.read_csv('INPUT HERE') #Input csv file containing users here!!!
addr_df.reset_index(drop=True,inplace=True)
addr_df_=addr_df.drop('Unnamed: 0',axis=1)
addr_df_.head()



def create_staging_table(cursor):
    cursor.execute("""
        DROP TABLE IF EXISTS INPUT_TABLE_NAME_HERE;    
        CREATE UNLOGGED TABLE INPUT_TABLE_NAME_HERE (
            user_login          TEXT,
            user_pwd            TEXT,
            user_email          TEXT,
            first_name          TEXT,
            last_name           TEXT,
            
        );""")

 





with conn.cursor() as cursor: #sending the table to psql
    create_staging_table(cursor)






def send_csv_to_psql(connection,csv,table_):
    sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    file = open(csv, "r")
    table = table_
    with connection.cursor() as cur:
        cur.execute("truncate " + table + ";")  #removes duplicate data
        cur.copy_expert(sql=sql % table, file=file)
        connection.commit()
#         cur.close()
#         connection.close()
    return connection.commit()

#This ^^^^ sends the csv to PSQL

send_csv_to_psql(conn,'CSV_NAME_HERE.csv','TABLE_NAME') #FILL IN THIS INFO OR IT WONT SEND TO OUR PAGE!!!



sql_="SELECT COUNT(*) FROM INPUT_TABLE_NAME"
cur.execute(sql_)
cur.fetchone()


cur.execute("SELECT * FROM INPUT_TABLE_NAME LIMIT 5")
cur.fetchall()

# Goals for this file:

#   This Python file --> Postgres Database <--> Webpage

#   This Python file  Query <--> QUERYED Postgres Database



