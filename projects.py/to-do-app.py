def task():
    tasks = []
    print("----WELCOME TO THE TASK MANGMENT APP----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\Stop"))
        if operation == 1:
            add = input("Enter task you want to add = ")