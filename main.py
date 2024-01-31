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
    print(tasks)


def mark_task_complete():
    pass
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