full_task = []
index = 0

def add_task():
    full_task.append(input_task)
    for index, task in enumerate(full_task, start=1):
        print(f"{index}:{task}")

def remove_task(index):
    full_task.pop(index - 1)
    for index, task in enumerate(full_task, start= 1):
        print(f"{index}: {task}")

while True:
    print('''\nWelcome to my todo-list
    choose your choose:
    a: to add the task
    r: to remove the task
    q: to quit ''')

    x = input("Choose: ")

    if x.lower() == "a":
        input_task = input("Your task: ")
        print("\n")
        add_task()
    if x.lower() == "r":
        index = int(input("Enter num of task you wanna del: "))
        print("\n")
        remove_task(index)
    if x.lower() == "q":
        quit()