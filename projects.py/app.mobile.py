contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")
    choice = input('Enter Your Choice = ')
    if choice == '1':
        name = input('Enter Your Name = ')
        if name is contacts:
            print(f"Contact Name {name} Already Exists!")
        else:
            age = input('Enter Age = ')
            email = input('Enter email = ')
            mobile = input('Enter Mobile Number = ')
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile}
            print(f"Contact Name {name} hasbeen created successfully")
    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age},Mobile Number: {mobile}')
        else:
            print("Contact not found")
    elif choice == '3':
        name = input('Enter Name to update contct = ')
        if name in contacts:
            age = input('Enter updated Age = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated Mobile Number = ')
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile}
        else:
            print('Contact not found')
    elif choice == '4':
        name = input("Enter contact name to delete = ")
        if name in contacts:
            del contacts[name]
            print(f"Contact Name {name} hasbeen deleted succesfully")
        else:
            print('Contact not found')
    elif choice == '5':
        search_name = input("Enter contact name to search = ")
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name {name}, Age: {age}, mobile number {mobile}, email {email}")
                found = True
        if not found:
            print("No contact found with that name")
    elif choice == '6':
        print(f"total in your book : {len(contacts)}")
    elif choice == '7':
        print(f"Good bye.... closing the program")
        break
    else:
        print("not found")