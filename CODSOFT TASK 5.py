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




