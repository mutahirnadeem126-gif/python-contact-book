
# Contact Book Project

contact = {}

while True:

    # Menu
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Contact
    if choice == 1:
        name = input("Enter the person name: ")
        number = input("Enter the person number: ")

        contact[name] = number

        print("Contact added successfully!")

    # View Contacts
    elif choice == 2:
        if len(contact) == 0:
            print("Contact Book is empty!")
        else:
            for name, number in contact.items():
                print("Name:", name, "| Number:", number)

    # Search Contact
    elif choice == 3:
        search_name = input("Enter the person name: ")

        if search_name in contact:
            print("Contact Found!")
            print("Name:", search_name)
            print("Number:", contact[search_name])
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == 4:
        contact_name = input("Enter the contact name: ")

        if contact_name in contact:
            del contact[contact_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Exit
    elif choice == 5:
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")
