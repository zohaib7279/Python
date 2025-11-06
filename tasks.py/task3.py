import sys
first = int(input("Enter first number: "))
def isinstance(first, str):
    print("please Enter the valid number")
    sys.exit()
second = input("Enter second number: ")
sum = first + second
diffrence = int(first) - int(second)
product = int(first) * int(second)
quotient = int(first) / int(second)
print(f"Sum = {sum} diffrence = {diffrence} product = {product} quotient = {quotient}")