grade = int(input("Enter student Marks = "))
if grade >= 90:
    print("Grade = A")
elif grade >= 80 and grade <= 90:
    print("Grade = B")
elif grade >= 70 and grade <= 80:
    print("Grade = C")
elif grade >= 60 and grade <= 70:
    print("Grade = D")
else:
    print("Failed")

