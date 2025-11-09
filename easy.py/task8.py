while True:
    try:
        ask1 = int(input("Enter the first number = "))
        ask2 = int(input("Enter the second number = "))
        ask3 = int(input("Enter the third number = "))
        store = [ask1 , ask2 , ask3]
        if ask1 > 20:
            print("Largest Number is = " ,ask1 or ask2 or ask3)
        elif ask2 > 20:
            print("Largest number is = " ,ask1 or ask2 or ask3)
        elif ask3 > 20:
            print("Largest number is = " ,ask1 or ask2 or ask3)
        else:
            print("Invalid option")
        break
    except:
        print("Enter the valid number")


