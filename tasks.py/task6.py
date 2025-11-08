while True:
    try:
        table = int(input("Enter the number = "))
        for i in range(1, 11):
            print(table, "X", i, "=", table * i)
        break
    except Exception:
        print("Please enter a valid number!")
