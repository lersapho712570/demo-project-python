from db_function import *



menu = """Please select one of the following options:
1) View user.
2) Add new user.
3) Update password.
4) Delete user.
5) Exists.

Your selection: """


create_user_table()

user_input=input(menu)

while user_input != "5":

    if user_input == "1":
        users = get_user()

        for user in users:
            print(user)
        print("\n")

    elif user_input == "2":

        id = input("User-ID: ")
        name = input("Name: ")
        department = input("Department: ")
        username = input("Username: ")
        password = input("Password: ")

        add_user(id,name,department,username,password)
    
    elif user_input == "3":
        username = input("Enter user id: ")
        new_password = input("New password: ")

        update_password(username,new_password)

    elif user_input == "4":
        delete_user(input("Enter Username: "))

    else:
        print("Invalid option, try again...")

    user_input=input(menu)

