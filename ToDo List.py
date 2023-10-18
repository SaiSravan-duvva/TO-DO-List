# Define Functions

# Function to display the to-do list
def display_list(todo_list):
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index. Please enter a valid task index.")

#  Implement the main function

def main():
    todo_list = []  # Initialize an empty to-do list

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the index of the task to remove: "))
                remove_task(todo_list, task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task index.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    main()  # Run the program

