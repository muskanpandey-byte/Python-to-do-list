import json

def save_tasks(tasks):
    with open("tasks.json", "w") as fp:
        json.dump(tasks, fp)

def load_tasks():
    try:
        with open("tasks.json", "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        return []

def todo_list():
    tasks = load_tasks()

    while True:
        choice = input("\nAdd / View / Remove / Exit : ").strip().lower()

        if choice == "add":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "view":
            if tasks:
                print("\nPending Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No pending tasks.")

        elif choice == "remove":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task removed successfully!")
            else:
                print("Task not found!")

        elif choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

todo_list()