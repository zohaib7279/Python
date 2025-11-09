while True:
    try:
        prime = int(input("Enter the number = "))
        if prime % 2 == 0:
            print(f"{prime} is not a prime number")
        else:
            print(f"{prime} is a prime number")
        break
    except ValueError:
        print("Please enter a valid integer")
        continue
        