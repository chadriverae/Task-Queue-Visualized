from TaskQueue_Visualized import *
print("Hello! Welcome to create-a-task-Queue!")
cycles_per_task = int(input('How many cycles would you like to reduce per task:'))
TQ = TaskQueue(cycles_per_task)
while True:
    print("Choose from the options below")
    print("1. Execute Tasks")
    print("2. Show Tasks")
    print("3. Add Task")
    print("4. Remove Task")
    choice = int(input())
    
    if choice == 1:
        TQ.execute_tasks()
        break

    if choice == 2:
        TQ.show_queue()
        print()
    
    if choice == 3:
        while True:
            print("Type \"q\" to exit to main screen")
            task_id = input("Enter ID of task you would like to add:")
            if task_id == "q":
                break
            cycles = int(input("Enter amount of cycles needed to complete task:"))
            TQ.add_task(Task(task_id, cycles))
            print("Task Added!\n")
        
    if choice == 4:
        task_id = input("Enter ID of task you would like to remove")
        TQ.remove_task(task_id)
        print("Task Removed!\n")
