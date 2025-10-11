light = "red"
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("The light was not exist" )

marks = int(input("marks of students :"))
if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"
print("Grade of the student ->" ,Grade)