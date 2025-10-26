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