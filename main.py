# Abdelwahed Jaouhari 
# To Do List Application

import json
from datetime import datetime


tasks = []

def main():
    message = """1 - Add tasks to a list
2 - Mark task as complete
3 - View tasks
4 - Delete task
5 - Save tasks to file
6 - Load tasks from file
7 - Quit"""


    while True:
        print(message)
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks_to_file()
        elif choice == "6":
            load_tasks_from_file()
        elif choice == "7":
            break
        else:
            print("Invalid choice, please enter a number between 1 and 7")

         
def add_task():
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Task will be added without a due date.")
        due_date = None

    task_info = {"task": task_description, "completed": False, "due_date": due_date}
    tasks.append(task_info)
    print("Task added to the list successfully")


def mark_task_complete():
    view_tasks(tasks)
    try:
        task_number = int(input("Choose the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid input, please enter a number")

def delete_task():
    view_tasks(tasks)
    try:
        task_number = int(input("Choose the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f'Task "{deleted_task["task"]}" deleted successfully')
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid input, please enter a number")

def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks to view")
        return

    for i, task in enumerate(tasks_list):
        status = "✔" if task["completed"] else "❌"
        due_date = f"Due on {task['due_date']}" if task['due_date'] else "No due date"
        print(f'{i + 1}. {task["task"]} [{status}] - {due_date}')
        print("-" * 30)

def save_tasks_to_file():
    filename = input("Enter the filename to save tasks to: ")
    # Convert due_date to string before saving
    tasks_to_save = [{"task": task["task"], "completed": task["completed"], "due_date": str(task["due_date"])}
                     for task in tasks]
    with open(filename, 'w') as file:
        json.dump(tasks_to_save, file, default=str)  # Use default=str to handle date serialization
    print(f'Tasks saved to {filename} successfully')

def load_tasks_from_file():
    filename = input("Enter the filename to load tasks from: ")
    try:
        with open(filename, 'r') as file:
            global tasks
            tasks = json.load(file)
        print(f'Tasks loaded from {filename} successfully')
    except FileNotFoundError:
        print(f'File {filename} not found')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from {filename}')

if __name__ == "__main__":
    main()