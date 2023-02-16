# =====importing libraries===========
'''This is the section where you will import libraries'''
import os.path
from datetime import datetime
from datetime import date

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Read file
user_file = open("user.txt", "r")
users_text = user_file.readlines()

# Save logins by username and password
logins = []
for line in users_text:
    line = line.strip("\n")
    login = line.split(", ")
    logins.append((login[0], login[1]))

# Close file
user_file.close()

# Receive login as user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# If login is incorrect, repeat
while not logins.__contains__((username, password)):
    print("Error: Login credentials not recognised")
    username = input("Enter your username: ")
    password = input("Enter your password: ")


def print_tasks_no_username():
    global tasks_file, line, task
    # Open tasks file
    tasks_file = open("tasks.txt", "r")
    # Save the lines from the file
    task_lines = tasks_file.readlines()
    # Create a list of tasks
    tasks = []
    for line in task_lines:
        # Split the task into parts
        line.strip("\n")
        task_parts = line.split(", ")

        # Save the task data to a dictionary
        task = {"assignee": task_parts[0], "title": task_parts[1], "description": task_parts[2],
                "assigned_date": task_parts[3], "due_date": task_parts[4], "task_complete": task_parts[5]}

        # Add the task to the list
        tasks.append(task)
    # If there are tasks saved
    if len(tasks) > 0:

        # Display all tasks
        for task in tasks:
            # Print opening banner
            print("-" * 40)

            # Print task information
            print("Task: " + str(task.get("title")))
            print("Assigned to: " + str(task.get("assignee")))
            print("Date assigned: " + str(task.get("assigned_date")))
            print("Due date: " + str(task.get("due_dates")))
            print("Task Complete?: " + str(task.get("task_complete")))
            print("Task description: " + str(task.get("description")))

        # Print closing banner
        print("-" * 40)
    # Close tasks file
    tasks_file.close()


def print_tasks(username):
    # Open tasks file
    tasks_file = open("tasks.txt", "r+")
    # Save the lines from the file
    task_lines = tasks_file.readlines()
    # Create a list of tasks
    tasks = []
    for line in task_lines:
        # Strip the newline character from the line
        line = line.strip("\n")
        # Split the task into parts
        task_parts = line.split(", ")

        # Save the task data to a dictionary
        task = {"assignee": task_parts[0], "title": task_parts[1], "description": task_parts[2],
                "assigned_date": task_parts[3], "due_date": task_parts[4], "task_complete": task_parts[5]}

        # Add the task to the list
        tasks.append(task)

    # If there are tasks saved
    if len(tasks) > 0:

        print("Tasks:")
        # Display all tasks assigned to the user
        for i, task in enumerate(tasks):
            # Check that task is assigned to user
            if task.get("assignee") == username:
                print(f"{i+1}. {task.get('title')}")

        while True:
            choice = input("Enter a task number to select it or enter -1 to go back to the main menu: ")
            if choice == "-1":
                break
            elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(tasks):
                print("Invalid choice. Please enter a valid task number or -1 to go back to the main menu.")
                continue
            else:
                task = tasks[int(choice) - 1]
                print("Task details:")
                print("Title:", task.get("title"))
                print("Assigned to:", task.get("assignee"))
                print("Date assigned:", task.get("assigned_date"))
                print("Due date:", task.get("due_date"))
                print("Task complete?", task.get("task_complete"))
                print("Description:", task.get("description"))
                while True:
                    edit_choice = input("Enter 'c' to mark the task as complete, 'e' to edit the task, or -1 to go back to the main menu: ")
                    if edit_choice == "-1":
                        break
                    elif edit_choice == "c":
                        if task.get("task_complete") == "No":
                            task["task_complete"] = "Yes"
                            tasks[int(choice) - 1] = task
                            tasks_file.seek(0)
                            tasks_file.truncate()
                            for t in tasks:
                                tasks_file.write(f"{t['assignee']}, {t['title']}, {t['description']}, {t['assigned_date']}, {t['due_date']}, {t['task_complete']}\n")
                            tasks_file.flush()
                            print("Task marked as complete.")
                        else:
                            print("Task is already complete.")
                        break
                    elif edit_choice == "e":
                        if task.get("task_complete") == "Yes":
                            print("This task has already been completed and cannot be edited.")
                            break
                        else:
                            edit_field = input("Enter 'u' to edit the assignee or 'd' to edit the due date: ")
                            if edit_field == "u":
                                new_assignee = input("Enter the new assignee: ")
                                task["assignee"] = new_assignee
                                tasks[int(choice) - 1] = task
                                tasks_file.seek(0)
                                tasks_file.truncate()
                                for t in tasks:
                                    tasks_file.write


def search_string_in_file(string, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if string in line:
                return True
    return False


def reg_user():
    ''' - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''

    # Ensure that the caller is an admin
    if username == "admin":

        # Receive username input
        new_username = input("Enter your new username: ")

        # Make sure username has not already been registered
        while search_string_in_file(new_username, "user.txt"):
            print("Error: Username already in use")
            new_username = input("Enter your new username: ")

        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm your new password: ")

        # Make sure passwords are equal
        while new_password != confirm_password:
            print("Error: Passwords do not match")
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")

        # Save the new username and password to file
        user_file = open("user.txt", "a")
        new_line = new_username + ", " + new_password
        user_file.write("\n" + new_line)
        user_file.close()

    else:
        print("Must be admin to register a new user")


def add_task():
    global task, tasks_file
    '''     - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
    # Receive user inputs
    assigned_username = input("Enter the username of the user assigned to this task: ")
    title = input("Enter the title of this task: ")
    description = input("Enter a description of this task: ")
    due_date = input("Enter the due date of this task: ")
    current_date = date.today()
    # Assemble task
    task = "\n" + assigned_username + ", " + title + ", " + description + ", " + str(
        current_date) + ", " + due_date + ", " + "No"
    # Open tasks file
    tasks_file = open("tasks.txt", "a")
    # Write task to file
    tasks_file.write(task)
    # Close tasks file
    tasks_file.close()


def view_all():
    ''' - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
    print_tasks_no_username()


def view_mine():
    ''' - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
    print_tasks(username)


def statistics():
    global tasks_file, user_file
    ''' Display statistics of the total number of tasks and
            the total number of users'''
    # Print opening banner
    print("-" * 40)
    # Count no. of tasks
    tasks_file = open("tasks.txt", "r")
    no_tasks = len(tasks_file.readlines())
    tasks_file.close()
    # Print no. of tasks
    print("Number of tasks: " + str(no_tasks))
    # Count no. of users
    user_file = open("user.txt", "r")
    no_users = len(user_file.readlines())
    user_file.close()
    # Print no. of users
    print("Number of users: " + str(no_users))
    # Print closing banner
    print("-" * 40)


def generate_reports():
    # Task overview report
    with open("task_overview.txt", "w") as task_file:
        # Count total number of tasks
        with open("tasks.txt", "r") as tasks:
            total_tasks = len(tasks.readlines())

        # Count number of completed and uncompleted tasks
        with open("tasks.txt", "r") as tasks:
            completed_tasks = 0
            uncompleted_tasks = 0
            overdue_tasks = 0
            today = date.today()
            for line in tasks:
                task_parts = line.strip().split(", ")
                if task_parts[5] == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    due_date = datetime.strptime((task_parts[4]), '%d %b %Y').date()
                    if due_date < today:
                        overdue_tasks += 1

        # Write task overview report to file
        task_file.write(f"Total number of tasks: {total_tasks}\n")
        task_file.write(f"Number of completed tasks: {completed_tasks}\n")
        task_file.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        task_file.write(f"Number of overdue tasks: {overdue_tasks}\n")
        task_file.write(f"Percentage of incomplete tasks: {uncompleted_tasks / total_tasks * 100:.2f}%\n")
        task_file.write(f"Percentage of overdue tasks: {overdue_tasks / total_tasks * 100:.2f}%\n")

    # User overview report
    with open("user_overview.txt", "w") as user_file:
        # Count total number of users
        with open("user.txt", "r") as users:
            total_users = len(users.readlines())

        # Count total number of tasks and tasks assigned to each user
        with open("tasks.txt", "r") as tasks:
            all_tasks = tasks.readlines()

        task_count_by_user = {}
        for line in all_tasks:
            task_parts = line.strip().split(", ")
            if task_parts[0] in task_count_by_user:
                task_count_by_user[task_parts[0]] += 1
            else:
                task_count_by_user[task_parts[0]] = 1

        # Write user overview report to file
        user_file.write(f"Total number of users: {total_users}\n")
        user_file.write(f"Total number of tasks: {total_tasks}\n")
        for user in task_count_by_user:
            user_tasks = task_count_by_user[user]
            user_percentage = user_tasks / total_tasks * 100
            completed_user_tasks = 0
            overdue_user_tasks = 0
            for line in all_tasks:
                task_parts = line.strip().split(", ")
                if task_parts[0] == user:
                    if task_parts[5] == "Yes":
                        completed_user_tasks += 1
                    else:
                        due_date = datetime.strptime((task_parts[4]), '%d %b %Y').date()
                        if due_date < today:
                            overdue_user_tasks += 1
            user_file.write(f"\n{user}\n")
            user_file.write(f"Number of tasks assigned to user: {user_tasks}\n")
            user_file.write(f"Percentage of total tasks assigned to user: {user_percentage:.2f}%\n")
            user_file.write(f"Percentage of assigned tasks completed: {completed_user_tasks / user_tasks * 100:.2f}%\n")
            user_file.write(f"Percentage of assigned tasks not completed: {100 * (user_tasks - completed_user_tasks) / user_tasks}%\n")


def display_statistics():
    # Check if the files exist and generate them if they don't
    if not os.path.isfile("task_overview.txt") or not os.path.isfile("user_overview.txt"):
        generate_reports()

    # Read the contents of the files and display the statistics
    with open("task_overview.txt", "r") as task_file, open("user_overview.txt", "r") as user_file:
        print("Task Overview:")
        print(task_file.read())
        print("User Overview:")
        print(user_file.read())


# MAIN
# Display options menu
while True:
    # Presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (Admin only)
s - Display statistics (Admin only)
a - Adding a task 
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    # Register User
    if menu == 'r':
        reg_user()

    # Statistics
    elif menu == 's':
        statistics()

    # Add Task
    elif menu == 'a':
        add_task()

    # View All
    elif menu == "va":
        view_all()

    # View Members
    elif menu == "vm":
        view_mine()

    # Generate Reports
    elif menu == "gr":
        generate_reports()

    # Display Statistics
    elif menu == "ds":
        display_statistics()

    # Exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")