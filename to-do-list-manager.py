import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                raise ValueError("Tasks file must contain a JSON list.")
            return tasks
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Warning: could not load tasks: {error}")
        return []


def save_tasks(tasks):
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2)
        return True
    except OSError as error:
        print(f"Error: could not save tasks: {error}")
        return False


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tags = input("Tags separated by commas (optional): ").strip()
    due_date = input("Due date (optional): ").strip()
    tasks.append({
        "title": title,
        "done": False,
        "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
        "due_date": due_date,
    })

    if save_tasks(tasks):
        print("Task added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done") else "Pending"
        details = f"{index}. [{status}] {task.get('title', '')}"
        tags = task.get("tags", [])
        due_date = task.get("due_date", "")
        if tags:
            details += f" (tags: {', '.join(tags)})"
        if due_date:
            details += f" (due: {due_date})"
        print(details)


def get_task_index(tasks):
    view_tasks(tasks)
    if not tasks:
        return None

    choice = input("Enter task number: ").strip()
    if not choice.isdigit():
        print("Please enter a valid task number.")
        return None

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return None
    return index


def delete_task(tasks):
    index = get_task_index(tasks)
    if index is None:
        return

    removed = tasks.pop(index)
    if save_tasks(tasks):
        print(f"Deleted: {removed.get('title', '')}")


def mark_task_done(tasks):
    index = get_task_index(tasks)
    if index is None:
        return

    tasks[index]["done"] = True
    if save_tasks(tasks):
        print(f"Marked done: {tasks[index].get('title', '')}")


def print_menu():
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task done")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()
