# create an array to save tasks in
tasks = []

def newTask():
    # ask user to enter their task
    task = input("Enter task: ")
    # add task to the program / tasks
    tasks.append(task)
    # print confirmation message for added task
    print(f"New '{task}' created to the list")

def viewTask():
    # if there is no task added, let the user know
    if not tasks:
        print("No tasks found!")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    # first show which tasks are available
    viewTask()
    try:
        # prompt user which task to delete
        taskToDelete = int(input("Choose # to delete: "))
        # if task exists the delete
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            # confirm task is deleted
            print(f"Task #{taskToDelete} deleted!")

        else:
            # if there are no tasks to delete, let user know
            print(f"Task #{taskToDelete} not found!!")

    except:
        print("Incorrect input!!")

# create a main method
if __name__ == "__main__":
# create a loop to run app
    print("To-Do-List App: ")
    while True:
        print("\nWhat would you like to do? ")
        print("-------------------------------")
        print("1. Add new task")
        print("2. Delete task")
        print("3. View Added tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
         # Add a task
            newTask()
        elif(choice == "2"):
         # Delete a task
            deleteTask()
        elif(choice == "3"):
         # view a task
            viewTask()
        elif(choice == "4"):
         # quit the program
            break
        else:
            print('Please enter a valid input!')
    print("See you soon!!!")
