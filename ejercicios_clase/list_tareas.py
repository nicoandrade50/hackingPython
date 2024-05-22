tasks = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if tasks:
            index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task deleted successfully!")
            else:
                print("Invalid index!")
        else:
            print("No tasks added yet!")
    elif choice == "3":
        if tasks:
            print("List of tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks added yet!")
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")





