import task_manager

print("\nTo-Do App\n")

while True:
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit\n")

    choice = input("Select an option: ")

    if choice == "1":
        task_manager.add_task()
    elif choice == "2":
        task_manager.list_tasks()
    elif choice == "3":
        task_manager.edit_task()
    elif choice == "4":
        task_manager.delete_task()
    elif choice == "5":
        print("\nGoodbye!\n")
        break
    else:
        print("Invalid choice!\n")