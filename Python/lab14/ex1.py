
import pickle
import os
import tkinter as tk
from tkinter import filedialog

PhoneBook = {}

Command = {
    "+": "add a new contact",
    "-": "delete a contact",
    "f": "find a contact",
    "p": "print out all contacts",
    "q": "quit the program",
    "s": "save contacts to a file",
    "l": "load contacts from a file"
}

root = tk.Tk()
root.withdraw()


def add_contact():
    
    phone_num = input("Enter the phone number: ")
    contact = input("Enter a contact: ")
    list = ["/", ".","?"]
    for i in contact:
        print(i)
        if i in list:
            raise RuntimeError("Invalid characters")
    PhoneBook[contact] = phone_num

while True:
    print("Phonebook Manager")
    for command, description in Command.items():
        print(f"Press {command} to {description}")
    command = input("Enter your command: ")

    if command == "+":
        try:
            add_contact()
        except RuntimeError as e:
            print(e)
                
        
        

    elif command == "-":
        contact = input("Enter the contact you want to delete: ")
        if contact in PhoneBook:
            PhoneBook.pop(contact, None)
            print(f"{contact} has been deleted from the phonebook.")
        else:
            print(f"Error: Contact '{contact}' not found in the phonebook.")

    elif command == "f":
        contact = input("Enter the contact you are searching for: ")
        if contact in PhoneBook:
            print(f"Phone no. {PhoneBook[contact]}")
        else:
            print(f"Error: Contact '{contact}' not found in the phonebook.")

    elif command == "p":
        for contact, phone_num in PhoneBook.items():
            print(f"Contact: {contact}, Phone No. {phone_num}")

    elif command == "s":
        file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle Files", ".pkl")])
        if file_path:
            try:
                with open(file_path, "wb") as file:
                    pickle.dump(PhoneBook, file)
                print(f"Contacts saved to {file_path}")
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
            except IOError:
                print(f"Error occurred while writing to file '{file_path}'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    elif command == "l":
        file_path = filedialog.askopenfilename(defaultextension=".pkl", filetypes=[("Pickle Files", ".pkl")])
        if file_path:
            try:
                with open(file_path, "rb") as file:
                    PhoneBook = pickle.load(file)
                print(f"Contacts loaded from {file_path}")
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
            except IOError:
                print(f"Error occurred while reading the file '{file_path}'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


    elif command == "q":
        break

    else:
        print("Invalid command. Please try again.")