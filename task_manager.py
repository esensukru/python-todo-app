from json_manager import load_tasks, save_tasks

def add_task():
    tasks = load_tasks()

    task = input("Enter a task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return
    
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1

    task_info = {
        "id": new_id,
        "task": task,
        "completed": False
    }

    tasks.append(task_info)

    save_tasks(tasks)

    print("\nTask added successfully.\n")


def list_tasks():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return
    
    print("\n")
    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['task']} | Completed: {task['completed']}")
    print("\n")


def edit_task():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    list_tasks()
    
    try:
        choice_id = int(input("Enter the task ID to edit: "))
    except ValueError:
        print("\nPlease enter a valid ID!\n")
        return

    for task in tasks:
        if task["id"] == choice_id:
            print("\n1. Task name")
            print("2. Completion status\n")

            choice = input("Select an option: ")

            if choice == "1":
                new_task = input("Enter the new task name: ").strip()

                if new_task == "":
                    print("\nTask name cannot be empty.\n")
                    return

                task["task"] = new_task

            elif choice == "2":
                task["completed"] = not task["completed"]

            else:
                print("\nInvalid choice.\n")
                return

            save_tasks(tasks)
            print("\nTask updated successfully.\n")
            return
        
    print("\nNo task found with this ID.\n")


def delete_task():
    tasks = load_tasks()
    
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return
    
    list_tasks()
    
    try:
        choice_id = int(input("Enter the task ID to delete: "))
    except ValueError:
        print("\nPlease enter a valid ID!\n")
        return
    
    for task in tasks:
        if task["id"] == choice_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("\nTask deleted successfully.\n")
            return

    print("\nNo task found with this ID.\n")