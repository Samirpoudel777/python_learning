tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
