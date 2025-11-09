while True:
    try:
        num = int(input("Enter a number to find factorial: "))
        
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
        break

    except ValueError:
        print("Please enter a valid integer")

        
