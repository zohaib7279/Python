print("----- Diary Application -----")
Date = ""
English = ""
Urdu = ""
Math = ""
Social = ""
Science = ""
Islamiyat = ""
while True:
    print("1. Add Diary")
    print("2. View Diary")
    print("3. Delete Diary")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice (1-5) = "))
        if choice == 1:
            Date = str(input("Enter The Date = "))
            English = str(input("Enter The English Diary = "))
            Urdu = str(input("Enter The urdu Diary = "))
            Math = str(input("Enter The math Diary = "))
            Social = str(input("Enter The Social Diary = "))
            Science = str(input("Enter The Science Diary = "))
            Islamiyat = str(input("Enter The Islamiyat Diary = "))
            print("Diary Added Successfully!")
        elif choice == 2:
            view_date = str(input("Enter The Date to View Diary = "))
            print(f"Diary for {view_date}:")
            print(f"English: {English}")
            print(f"Urdu: {Urdu}")
            print(f"Math: {Math}")
            print(f"Social: {Social}")
            print(f"Science: {Science}")
            print(f"Islamiyat: {Islamiyat}")
        elif choice == 3:
            delete_date = str(input("Enter The Date to Delete Diary = "))
            Date = ""
            English = ""
            Urdu = ""
            Math = ""
            Social = ""
            Science = ""
            Islamiyat = ""
            print("Diary Deleted Successfully!")
        elif choice == 4:
            print("Closing the Diary Application....")
            break
    except ValueError:
        print("Invalid input. Please try again.")