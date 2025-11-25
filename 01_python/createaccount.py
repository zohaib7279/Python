want = input("Do you want to create an account? (yes/no): ")

while True:
    try:
        if want == "yes":
            print("----- CREATE ACCOUNT APP -----") 
            account_list = []
            account_messege = []

            while True:
                print("1. Add account")
                print("2. View account")
                print("3. Delete account")
                print("4. Activate account")
                print("5. Send Message")
                print("6. View Messages")
                print("7. Delete all messages")
                print("8. Display All Account And All Messages")
                print("9. View Activate Account")
                print("10. Exit")

                try:
                    account = int(input("Enter the number to perform function = "))
                except:
                    print("Please enter a valid number")
                    continue

                if account == 1:
                    new_username = input("Enter your username: ")
                    while True:
                        if new_username == "":
                            print("Username cannot be empty.")
                            new_username = input("Enter your username: ")
                        elif new_username == "1234567890":
                            print("Username cannot be a sequence of numbers.")
                            new_username = input("Enter your username: ")
                        else:
                            break

                    new_password = input("Enter your password: ")
                    while True:
                        if new_password == "":
                            print("Password cannot be empty.")
                            new_password = input("Enter your password: ")
                        elif len(new_password) < 8:
                            print("Password must be at least 8 characters long.")
                            new_password = input("Enter your password: ")
                        else:
                            break

                    confirm_password = input("Confirm your password: ")
                    while True:
                        if confirm_password != new_password:
                            print("Passwords do not match.")
                            confirm_password = input("Confirm your password: ")
                        else:
                            break
                    

                    email = input("Enter your email: ")
                    while True:
                        if "@" not in email or "." not in email:
                            print("Invalid email format.")
                            email = input("Enter your email: ")
                        if email == "":
                            print("Email cannot be empty.")
                            email = input("Enter your email: ")
                        elif "gmail.com" not in email and "yahoo.com" not in email and "outlook.com" not in email:
                            print("Email must be from gmail, yahoo, or outlook.")
                            email = input("Enter your email: ")
                        else:
                            break

                    phone_number = input("Enter your phone number: ")
                    while True:
                        if phone_number == "":
                            print("Phone number cannot be empty.")
                            phone_number = input("Enter your phone number: ")
                        elif phone_number == "1234567890":
                            print("Phone number cannot be a sequence of numbers.")
                            phone_number = input("Enter your phone number: ")
                        elif phone_number == "0000000000":
                            print("Phone number cannot be all zeros.")
                            phone_number = input("Enter your phone number: ")
                        elif len(phone_number) > 15 or len(phone_number) < 10:
                            print("Phone number must be between 10 and 15 digits.")
                            phone_number = input("Enter your phone number: ")
                        else:
                            break

                    account_data = {
                        "username": new_username,
                        "password": new_password,
                        "email": email,
                        "phone": phone_number
                    }

                    account_list.append(account_data)
                    print("Account added successfully!")

                elif account == 2:
                    if len(account_list) == 0:
                        print("No accounts found. Please add an account first.")
                    else:
                        print(f"{account_list}")

                elif account == 3:
                    delete = input("Enter username to delete OR type 'all': ")
                    if delete == "all":
                        account_list.clear()
                        print("All accounts deleted.")
                    else:
                        if len(account_list) == 0:
                            print("No accounts found. Please add an account first.")
                        else:
                            if delete == ["username"]:
                                account_list.clear(["username"])
                                print(f"Account '{delete}' deleted.")
                            else:
                                print(f"Account '{delete}' not found.")

                elif account == 4:
                    activate = input("Enter account username to activate = ")
                    if len(account_list) == 0:
                        print("No accounts found. Please add an account first.")
                    else:
                        print(f"Account '{activate}' is now activated.")

                elif account == 5:
                        recipient = input("To : ")
                        while True:
                            try:
                                if recipient == "":
                                    print("Recipient cannot be empty.")
                                    recipient = input("To : ")
                                elif recipient != "." and "@" not in recipient:
                                    print("Invalid characters in recipient field.")
                                    recipient = input("To : ")
                                elif ("gmail.com" not in recipient and 
                                "yahoo.com" not in recipient and 
                                "outlook.com" not in recipient):
                                    print("Email must be from gmail,yahoo,or outlook.")
                                    recipient = input("To : ")
                                else:
                                    break
                            except:
                                print("An error occurred. Please try again.")
                                recipient = input("To : ")
                                continue
                        sender = input("From : ")
                        while True:
                            try:
                                if sender == "":
                                    print("Sender cannot be empty.")
                                    sender = input("From : ")
                                elif sender is not "." and "@" not in sender:
                                    print("Invalid characters in sender field.")
                                    sender = input("From : ")
                                else:
                                    break
                            except:
                                print("An error occurred. Please try again.")
                                sender = input("From : ")
                                continue
                        ent_messege = input("Enter your message: ")
                        account_messege.append({"to": recipient, "from": sender, "message": ent_messege})
                        print("Message sent!")

                elif account == 6:
                    if len(account_messege) == 0:
                        print("No messages to display.")
                    else:
                        print(account_messege)

                elif account == 7:
                    account_messege.clear()
                    print("All messages have been deleted.") 

                elif account == 8:
                    print("Accounts:", account_list)
                    print("Messages:", account_messege)

                elif account == 9:
                    if len(account_list) == 0:
                        print("No accounts found. Please add an account first.")
                    else:
                        print("Activated Accounts:", activate)

                elif account == 10:
                    print("Exiting the application. Goodbye!")
                    break

                else:
                    print("Invalid choice, enter a number between 1–10.")

        elif want == "no":
            print("Thank you! but account creation app is very useful.")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

        break

    except:
        print("An error occurred. Please try again.")
        break
