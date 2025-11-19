a = input("Enter your name = ")
b = input("Enter your age = ")
c = input("Enter your city = ")
d = input("Enter your country = ")
print(f"my name is {a}, my age is {b}, I live in {c}., my country is {d}")
e = input("Enter your feedback (happy , sad)= ")
while True:
    try:
        if e == "happy":
            print("Thanks for send yuor feedback")
        elif e == "sad":
            print("ok but your feedback are very sad in my heart")
        else:
            print("Invalid feedback")
    except e == "sad":
        print("An error occurred")
    break