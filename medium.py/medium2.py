# step 1: start
# step 2: create a loop that continues until a valid integer is entered
while True:
    # step 3: try to get user input and convert it to an integer
    try:
        # tep 4: ask user for input
        prime = int(input("Enter the number = "))
        # step 5: check if the number is prime
        if prime % 2 == 0:
            print(f"{prime} is not a prime number")
        # step 6: else print that it is prime and not prime
        else:
            print(f"{prime} is a prime number")
        # step 7: break the loop 
        break
    # step 8: The try are code are correct if the code are not correct then except this code will run
    except ValueError:
        print("Please enter a valid integer")
        continue
# step 9: end
        