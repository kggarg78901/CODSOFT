
##    ________________________TASK-1__________________________ 


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task", task,"added to the list.")

    def mark_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task", task,"marked as completed.")
        else:
            print("Task", task,"not found in the list.")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print("{i}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter the task to mark as completed: ")
            todo.mark_completed(task)
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("Thanks for using the application. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()






