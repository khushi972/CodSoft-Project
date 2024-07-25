#todo_list = []
completed_tasks = []

def display_menu():
    print("Welcome to the To-Do List Application!")
    print("Please select an option:")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View pending tasks")
    print("4. View completed tasks")
    print("5. Remove a task")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

def mark_as_completed():
    if not todo_list:
        print("The to-do list is empty.")
        return

    print("Pending tasks:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

    task_index = int(input("Enter the number of the task to mark as completed: "))
    if task_index < 1 or task_index > len(todo_list):
        print("Invalid task number.")
        return

    completed_task = todo_list.pop(task_index - 1)
    completed_tasks.append(completed_task)
    print(f"Task '{completed_task}' has been marked as completed.")

def view_pending_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("Pending tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def view_completed_tasks():
    if not completed_tasks:
        print("No completed tasks.")
    else:
        print("Completed tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    if not todo_list:
        print("The to-do list is empty.")
        return

    print("Pending tasks:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

    task_index = int(input("Enter the number of the task to remove: "))
    if task_index < 1 or task_index > len(todo_list):
        print("Invalid task number.")
        return

    removed_task = todo_list.pop(task_index - 1)
    print(f"Task '{removed_task}' has been removed from the to-do list.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_as_completed()
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            view_completed_tasks()
        elif choice == "5":
            remove_task()
        elif choice == "6":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
