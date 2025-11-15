mul = int(input("Enter The Number = "))  
print(f"It is very simple lets read the table of {mul} =")                     
for i in range(1,11):
    print(mul ,"x", i, "=", mul*i)
    continue
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Program ended.")
        break

    print("You entered:", num)