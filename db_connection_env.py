import sys,os
import psycopg2
from config import *

# os.environ['dbname'] = 'postgres'
# os.environ['dbuser'] = 'postgres'
# os.environ['dbpassword'] = 'P@ssw0rd'
# os.environ['dbhost'] = 'localhost'
# os.environ['dbport'] = '5432'
# os.environ['NODE_NAME'] = 'worker-node01'

# Create database connection
def new_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('dbname'),
            user=os.getenv('dbuser'),
            password=os.getenv('dbpassword'),
            host=os.getenv('dbhost'),
            port=os.getenv('dbport')            
        )

    except Exception as error:
        print(error)
        # sys.exit(1)
    
    return connection



