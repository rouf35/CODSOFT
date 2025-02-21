def task():
    tasks = []
    print("Welcome to the Task Manager")
    
    total_task = int(input("Enter how many tasks you want to add ="))
    for i in range(1, total_task+1):    
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter \1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n")) 
        if operation == 1:
            add = input("Enter task to add = ")
            tasks.append(add)
            print(f"Task {add} added successfully")

        elif operation == 2:
            updated_val = input("Enter task name you want to update = ")
            if updated_val in tasks:
                update = input("Enter updated task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = update
                print(f"Task {updated_val} updated to {update}")

        elif operation == 3:
            del_val = input("Enter task name you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} deleted successfully")

        elif operation == 4:
            print(f"Total tasks are\n{tasks}")

        elif operation == 5:
            print("Thank you for using Task Manager")
            break

        else:
            print("Invalid input")

task()