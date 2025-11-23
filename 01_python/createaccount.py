print("----- CREATE ACCOUNT APP -----") 
account_list = []   # store multiple accounts
while True:
    print("1. Add account")
    print("2. View account")
    print("3. Delete account")
    print("4. Exit")
    try:

        account = int(input("Enter the number to perform function = "))

        if account == 1:
            new_username = input("Enter your username: ")
            while True:
                try:
                    if new_username == "":
                        print("Username cannot be empty.")
                        new_username = input("Enter your username: ")
                    elif new_username == "1234567890":
                        print("Username cannot be a sequence of numbers.")
                        new_username = input("Enter your username: ")
                    else:
                        print("Username is valid.")
                        break
                except:
                    print("An error occurred. Please try again.")
                    new_username = input("Enter your username: ")

            new_password = input("Enter your password: ")

            while True:
                try:
                    if new_password == "":
                        print("Password cannot be empty.")
                        new_password = input("Enter your password: ")
                    else:
                        print("Password is valid.")
                        break
                except:
                    print("An error occurred. Please try again.")
                    new_password = input("Enter your password: ")

            confirm_password = input("Confirm your password: ")

            while True:
                try:
                    if confirm_password != new_password:
                        print("Passwords do not match.")
                        confirm_password = input("Confirm your password: ")
                    else:
                        print("Passwords match.")
                        break
                except:
                    print("An error occurred. Please try again.")
                    confirm_password = input("Confirm your password: ")

            email = input("Enter your email: ")

            while True:
                try:
                    if "@" not in email or "." not in email:
                        print("Invalid email format.")
                        email = input("Enter your email: ")
                    else:
                        print("Email is valid.")
                        break
                except:
                    print("An error occurred. Please try again.")
                    email = input("Enter your email: ")

            phone_number = input("Enter your phone number: ")

            while True:
                try:
                    if phone_number == "":
                        print("Phone number cannot be empty.")
                        phone_number = input("Enter your phone number: ")
                    else:
                        print("Phone number is valid.")
                        break
                except:
                    print("An error occurred. Please try again.")
                    phone_number = input("Enter your phone number: ")

            # Save account
            account_data = {
                "username": new_username,
                "password": new_password,
                "email": email,
                "phone": phone_number
            }

            account_list.append(account_data)
            print("Account added successfully!")

        elif account == 2:
            print(account_list)
            if len(account_list) == 0:
                print("No add account please add account and view")

        elif account == 3:
            delete = input("Enter account number to delete = ")
            if delete == "all":
                del account_list
            else:
                pass

        elif account == 4:
            print("Closing the app.....")
            break

        else:
            print("Invalid choice please enter the valid number in 1-4")
    except:
        print("please enter the valid number")