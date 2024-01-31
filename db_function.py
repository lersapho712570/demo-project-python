from db_connection_env import *
        

# Project Function
def db_status():
    connection = new_connection()

    if connection is not None:
        create_user_table()
        return True
    else:
        return False

def create_project_table():
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS projects (no TEXT, customer TEXT, project_name TEXT, status TEXT);"
    )
    connection.commit()
    cur.close()
    connection.close()

def add_project(no,customer,project_name,status):
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO projects (no, customer, project_name, status) VALUES (%s, %s, %s, %s);",(no,customer,project_name,status))
    connection.commit()
    cur.close()
    connection.close()

def delete_project(project):
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(f"DELETE FROM projects WHERE project_name = '{project}';")
    connection.commit()
    cur.close()
    connection.close()

def get_project():
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM projects ORDER BY customer;")
    users = cur.fetchall()
    for user in users:
        print(user)
    cur.close()
    connection.close()


# User Function
def create_user_table():
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id TEXT, name TEXT, department TEXT, username TEXT, password TEXT);"
    )
    connection.commit()
    cur.close()
    connection.close()

def add_user(id,name,department,username,password):
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO users (id, name, department , username, password) VALUES (%s, %s, %s, %s, %s);",(id,name,department,username,password)
    )
    connection.commit()
    cur.close()
    connection.close()

def update_password(username,new_password):
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{username}';")
    connection.commit()
    cur.close()
    connection.close()

def delete_user(user):
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(f"DELETE FROM users WHERE username = '{user}';")
    connection.commit()
    cur.close()
    connection.close()

def get_user():
    connection = new_connection()
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM users ORDER BY id;")
    users = cur.fetchall()
    cur.close()
    connection.close()
    return users