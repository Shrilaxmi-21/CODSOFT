def task():
    tasks = []
    print("------ WELCOME TO THE TO DO LIST ------")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print("Today's tasks are:")
    print(tasks)

    run = True

    while run:
        operation = int(input(
            "Enter operation:"
            "1. Add"
            "2. Update"
            "3. Delete"
            "4. View"
            "5. Exit"
            "Enter your choice = "
        ))

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print("Task added successfully.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif operation == 3:
            delete_task = input("Enter the task name you want to delete = ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("\nYour tasks are:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        elif operation == 5:
            print("Exiting To-Do List. Goodbye!")
            run = False 

        else:
            print("Invalid choice. Please try again.")

task()
