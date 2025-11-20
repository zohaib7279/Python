# print("----- login app -----")
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "1234":
#     print("Login successful!")
# else:
#     print("Login failed. Please check your username and password.")
print("----- create account app -----")
new_username = input("Enter your username: ")
new_password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
date_birth = input("Enter your date of birth (DD/MM/YYYY): ")
email = input("Enter your email address: ")
sign_out = input("Do you want to sign out? (yes/no): ")
while True:
    try:
        if new_password == confirm_password:
            print("Account created successfully!")
        elif len(new_password) < 8:
            print("Password must be at least 8 characters long.")
        elif "@" not in email or ".":
            print("Invalid email address.")
        elif new_username == "":
            print("Username cannot be empty.")
        elif new_username == "1234567890":
            print("Username cannot be a sequence of numbers.")
        elif date_birth == "":
            print("Date of birth cannot be empty.") 
        elif date_birth >= 2000:
            valid_age = input("Enter your date birt in DD/MM/YYYY format: ")
        elif sign_out == "no":
            print("You are still signed in.")
        elif sign_out == "yes":
            print("You have signed out.")
        break
    except:
        print("An error occurred. Please try again.")
task = input("Do you want to see the account? (yes/no): ")
if task == "yes":
    print("Username:", new_username)
    print("Date of Birth:", date_birth)
    print("Email:", email)
elif task == "no":
    print("Thank you for using the account creation app.")