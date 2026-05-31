todo_List = []

while True:
    print ("\n--- TO DO LIST ---")
    print ("1. View task")
    print ("2. Add task")
    print ("3. Remove Tasks")
    print ("4. 4Exit")

    choice = input ("Choose an option (1-4): ")

    if choice == "1":
        if not todo_List:
            print ("Your to-do list is empty!")
        else:
            print ("\nYOUR TASKS:")
            for i, task in enumerate(todo_List, start = 1):
                print (f"{i}. {task}")

    elif choice == "2":
        new_task = input ("Enter your task: ")
        todo_List.append (new_task)
        print (f"Added: '{new_task}'")

    elif choice == "3":
        if not todo_List:
            print("Nothing to remove. List is empty!")
        else:
            print ("Nothing to remove. List is empty!")
            for i, task in enumerate(todo_List, start=1):
                print(f"{i}. {task}")

                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(todo_List):
                        removed = todo_List.pop(task_num -1)
                        print(f"Removed: '{removed}'")
                    else:
                        print ("Invalid task number!")
                except ValueError:
                    print("Please enter a valid numbr!")

    elif choice == "4":
        print ("Goodbye! Have a productive day!")
        break

    else:
        print ("Invalid Input! Please enter a number 1, 2, 3 or 4.")
