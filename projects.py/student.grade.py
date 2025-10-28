student_grades = {  }
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")
def updated(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are Updated {grade}")
    else:
        print(f"{name}has not found")    