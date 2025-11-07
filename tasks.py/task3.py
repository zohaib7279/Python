first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
try:
    sum_ = first + second
    difference = first - second
    product = first * second
    quotient = first / second
except ValueError:
    print("Invalid input")