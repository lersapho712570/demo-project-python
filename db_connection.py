import sys
import psycopg2
from config import *


# Create database connection
def new_connection():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)

    except Exception as error:
        print(error)
        sys.exit(1)
    
    return connection
