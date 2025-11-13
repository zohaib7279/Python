# step 1: start
# step 2: create while loop to calculate factorial and user input
while True:
    try:
        num = int(input("Enter a number to find factorial: "))
        # step 3: create the factorial function
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        # step 4: call the factorial function and print the result
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
        # step 5: break the loop
        break
    # step 6: handle invalid input
    except ValueError:
        print("Please enter a valid integer")
# step 7: end

        
