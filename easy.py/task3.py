while True:
    try:
        first = int(input("Enter the first number = "))
        second = int(input("Enter the second number = "))
        sum = int(first) + int(second)
        diffrence = int(first) - int(second)
        product = int(first) * int(second)
        qoutient = int(first) / int(second)
        break
    except:
        print("please enter the valid number")
print(f"Sum = {sum} diffrence = {diffrence} product = {product} qoutient = {qoutient}")