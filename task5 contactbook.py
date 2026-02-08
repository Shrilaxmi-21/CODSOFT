def contact_book():
    contacts = []
    run = True

    print("------ WELCOME TO CONTACT BOOK ------")

    while run:
        print("Choose an option:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter name = ")
            phone = input("Enter phone number = ")
            email = input("Enter email = ")
            address = input("Enter address = ")

            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            contacts.append(contact)
            print("Contact added successfully.")
        elif choice == 2:
            if not contacts:
                print("No contacts available.")
            else:
                print("Contact List:")
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. {c['name']} - {c['phone']}")
        elif choice == 3:
            search = input("Enter name or phone to search = ")
            found = False

            for c in contacts:
                if search == c["name"] or search == c["phone"]:
                    print("Contact Found:")
                    print("Name:", c["name"])
                    print("Phone:", c["phone"])
                    print("Email:", c["email"])
                    print("Address:", c["address"])
                    found = True

            if not found:
                print("Contact not found.")
        elif choice == 4:
            name = input("Enter the name of contact to update = ")
            found = False

            for c in contacts:
                if c["name"] == name:
                    c["phone"] = input("Enter new phone = ")
                    c["email"] = input("Enter new email = ")
                    c["address"] = input("Enter new address = ")
                    print("Contact updated successfully.")
                    found = True

            if not found:
                print("Contact not found.")
        elif choice == 5:
            name = input("Enter the name of contact to delete = ")
            found = False

            for c in contacts:
                if c["name"] == name:
                    contacts.remove(c)
                    print("Contact deleted successfully.")
                    found = True

            if not found:
                print("Contact not found.")

        elif choice == 6:
            print("Exiting Contact Book. Goodbye!")
            run = False

        else:
            print("Invalid choice. Try again.")
contact_book()