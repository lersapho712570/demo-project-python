from db_function import *



menu = """Please select one of the following options:
1) View project.
2) Add new project.
3) Delete project.
4) Exists.

Your selection: """


create_project_table()

user_input=input(menu)

while user_input != "4":

    if user_input == "1":
        get_project()
        print("\n")

    elif user_input == "2":

        no = input("Project No: ")
        customer = input("Customer Name: ")
        project_name = input("Project Name: ")
        status = input("Remark: ")
        add_project(no,customer,project_name,status)
    
    elif user_input == "3":
        project = input("Delete Project: ")
        delete_project(project)

    else:
        print("Invalid option, try again...")

    user_input=input(menu)

