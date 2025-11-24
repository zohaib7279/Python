want = input("Do you want to create an account? (yes/no): ")

while True:
    try:
        if want == "yes":
            print("----- CREATE ACCOUNT APP -----") 
            account_list = []
            account_messege = []

            while True:
                print("\n1. Add account")
                print("2. View account")
                print("3. Delete account")
                print("4. Sign out")
                print("5. Send Message")
                print("6. View Messages")
                print("7. Delete all messages")
                print("8. Display All Account And All Messages")
                print("9. Exit")

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
                    while confirm_password != new_password:
                        print("Passwords do not match.")
                        confirm_password = input("Confirm your password: ")

                    email = input("Enter your email: ")
                    while "@" not in email or "." not in email:
                        print("Invalid email format.")
                        email = input("Enter your email: ")

                    phone_number = input("Enter your phone number: ")
                    while phone_number == "" or len(phone_number) < 10 or len(phone_number) > 15:
                        if phone_number == "":
                            print("Phone number cannot be empty.")
                        else:
                            print("Phone number must be between 10 to 15 digits.")
                        phone_number = input("Enter your phone number: ")

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
                        print(account_list)

                elif account == 3:
                    delete = input("Enter username to delete OR type 'all': ")
                    if delete == "all":
                        account_list.clear()
                        print("All accounts deleted.")
                    else:
                        found = False
                        for acc in account_list:
                            if acc["username"] == delete:
                                account_list.remove(acc)
                                found = True
                                print("Account deleted.")
                                break
                        if not found:
                            print("Account not found.")

                elif account == 4:
                    print("Signing out.....")

                elif account == 5:
                        recipient = input("To : ")
                        sender = input("From : ")
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
