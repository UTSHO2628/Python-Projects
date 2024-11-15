def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_number = int(input("Enter task number to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice.")

todo_list()

