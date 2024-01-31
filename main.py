# Abdelwahed Jaouhari 
# To Do List Application

def add_task():
    #get task from user 
    task = input("Enter task: ")
    #define task status
    task_info = {"task": task, "completed": False,}
    # add task to the list of tasks
    tasks.append(task_info)
    print("Task added to the list successfuly")


def mark_task_complete():
    # get list of incomplete tasks 
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    
    # show them to the user 
    for i, task in enumerate(incomplete_tasks):
        print(f'{i+1}- {task["task"]}')
        print("-"*30)
    # get the task from the user 
    task_number = int(input("Choose the task to complete:"))
    # mark the task as completed 
    incomplete_tasks[task_number - 1]["completed"] = True
    # print a message to the user 
    print(tasks)
def view_tasks():
    ...

    

message = """1 - Add tasks to a list
2 - Mark task as complete
3 - View tasks
4 - Quit """

tasks = []

while True:
    print(message)
    choice = input ("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_complete()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4")