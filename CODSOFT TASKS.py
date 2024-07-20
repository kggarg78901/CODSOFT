
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






##     _____________________TASK-2______________________


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation. Please choose +, -, *, or /."

print(f"Result: {result}")





##    ________________________TASK-3__________________________ 


import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        desired_len = int(input("Enter the desired password length- "))
        if desired_len <= 0:
            print("Please enter a positive integer for the password length.")
            return

        generated_password = generate_password(desired_len)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()




## _____________________TASK-5 _________________________


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if len(phone_number) != 10:
            print("\nPlease enter a valid Phone number!")
            return
        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address":address
        }
        print(f"\nContact added successfully!")

    def display_all_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("---")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email: {self.contacts[name]['email']}")
            print(f"Address: {self.contacts[name]['address']}")
        else:
            print("\n----Contact not found!")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]["phone_number"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print(f"\n---Contact {name} updated successfully!---")
        else:
            print("\n---Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact {name} deleted successfully!")
        else:
            print("\nContact not found!")

    
def main():
    contact_manager = ContactManager()
    while True:
        print("\n--------CONTACT MANAGEMENT SYSTEM----------")
        print("\n1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("\nEnter your choice (1,2,3,4,5,6)- ")
        
        if choice == "1":
            name = input("Enter name- ")
            phone_number = input("Enter phone number- ")
            email = input("Enter email- ")
            address = input("Enter address- ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_manager.display_all_contacts()    

        elif choice == "3":
            name = input("Enter name- ")
            contact_manager.search_contact(name)
            
        elif choice == "4":
            name = input("\nEnter name of contact you want to update: ")
            phone_number = input("Enter new phone number (press enter to skip)- ")
            email = input("Enter new email (press enter to skip)- ")
            address = input("Enter new address (press enter to skip)- ")
            contact_manager.update_contact(name, phone_number, email, address)
            
        elif choice == "5":
            name = input("\nEnter name of contact you want to delete- ")
            contact_manager.delete_contact(name)
            
        elif choice == "6":
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
























