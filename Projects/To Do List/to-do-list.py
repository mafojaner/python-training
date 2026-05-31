todo_List = []

print ("\n--- TO DO LIST ---")
print ("1. View task")
print ("2. Add task")
print ("Remove Tasks")
print ("Exit")

choice = input ("Choose an option (1-4): ")

if choice == "1":
    print ("This language is tuff")
    
elif choice == "2":
    new_task = input ("Enter your task: ")
    todo_List.append (new_task)
    print (f"Added: '{new_task}'")
#elif choice == "3":
#elif choice == "4":
else:
    print ("Invalid Input! Please enter a number 1, 2, 3 or 4.")
