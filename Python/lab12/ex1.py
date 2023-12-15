def usermenu():
    print("Phonebook Manager")
    print("Press '+' to add a new contact.")
    print("Press '-' to delete a contact.")
    print("Press 'f' to find a contact.")
    print("Press 'p' to print out all contacts in the phonebook.")
    print("Press 'q' to quit the program.")
def bookmanager():
    phonebook = [] 
    while True:
        usermenu()
        user_choice = input("Enter the command of your choice: ")

        if user_choice == '+':
            add_contact(phonebook)
        elif user_choice == '-':
            delete_contact(phonebook)
        elif user_choice == 'f':
            find_contact(phonebook)
        elif user_choice == 'p':
            print_contacts(phonebook)
        elif user_choice == 'q':
            print("Quitting program.")
            break
        else:
            print("Invalid command. Please enter a valid command.")

def add_contact(phonebook):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    contact = {'name': name, 'phone': phone}
    phonebook.append(contact)


def delete_contact(phonebook):
    name = input("Enter the name of the contact to delete: ")
    for contact in phonebook:
        if contact['name'] == name:
            phonebook.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def find_contact(phonebook):
    name = input("Enter the name to find: ")
    for contact in phonebook:
        if contact['name'] == name:
            print("Contact found:")
            print_contact(contact)
            return
    print("Contact not found.")

def print_contacts(phonebook):
    print("All contacts in the phonebook:")
    if not phonebook:
        print("No contacts in the phonebook.")
    else:
        for contact in phonebook:
            print_contact(contact)

def print_contact(contact):
    print(f"Name: {contact['name']}, Phone: {contact['phone']}")


    

bookmanager()