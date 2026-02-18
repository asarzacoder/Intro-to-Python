"""
Project: Command Line To-Do List Manager
"""

tasks = []
complete = []

def delete_task(task_list, complete_list):

    view_task(task_list, complete_list)
    task_delete = int(input("Enter task number to delete >> "))

    while task_delete < 1 or task_delete > len(task_list):
        print("Invalid Input, try again.")
        task_delete = int(input("Enter task number to delete >> "))

    index = task_delete - 1
    task_list.pop(index)
    complete_list.pop(index)

def mark_task_complete(task_list, complete_list):

    view_task(task_list, complete_list)
    check_task = int(input("Enter task number to check off >> "))

    # Validate input is within list range
    while check_task < 1 or check_task > len(task_list):
        print("Invalid Input, try again.")
        check_task = int(input("Enter task number to check off >> "))
    print()

    index = check_task - 1
    complete_list[index] = True

def view_task(task_list, complete_list):
    if len(task_list) == 0:
        print("------------------------------")
        print("No task")
        print("------------------------------")
        return None
    else:
        print("------------------------------")
        for to_do in range(len(task_list)):
            print(f"{to_do+1}: {task_list[to_do]}", end=" ")

            if not complete_list[to_do]:
                print("[ ]")
            else:
                print("[X]")
        print("------------------------------")
    print()
    return None

def add_task(task_list, complete_list):
    append_task = input("Input Task >> ")
    task_list.append(append_task)
    complete_list.append(False)

    option = input("| 1) Add more task | 2) Menu | >> ")
    while option == str(1):
        append_task = input("Input Task >> ")
        task_list.append(append_task)
        complete_list.append(False)

        option = input("| 1) Add more task | 2) Menu | >> ")

def print_menu():
    print("1) Add Task")
    print("2) View Task")
    print("3) Mark Task Complete")
    print("4) Delete Task")
    print("5) Quit")
    menu_choice = int(input(">>> "))

    return menu_choice

quit_prog = False
while not quit_prog:
    user_option = print_menu()

    # Validate option in range 1 - 5
    while user_option < 1 or user_option > 5:
        print("Invalid option, please try again.")
        user_option = print_menu()

    if user_option == 1:
        add_task(tasks, complete)
    elif user_option == 2:
        view_task(tasks, complete)
    elif user_option == 3:
        mark_task_complete(tasks, complete)
    elif user_option == 4:
        delete_task(tasks, complete)
    elif user_option == 5:
        print("GOODBYE")
        quit_prog = True
        break