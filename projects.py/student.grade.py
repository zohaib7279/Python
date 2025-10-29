student_grades = {  }
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are Updated {grade}")
    else:
        print(f"{name}\nhas not found")    
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} hasbeen succesfully deleted")
    else:
        print(f"{name}has not found") 
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print(f"no student found/added")


def main():
    while True:
        print("\n Student Grade Managmaent System")
        print("1. Add Students")
        print("2. Update Students")
        print("3. Delete Students")
        print("4. View Students")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter Your grade = "))
            add_student(name,grade)
        elif choice == 2:
            name = input("Enter updated student name = ")
            grade = int(input("Enter Your updated grade = "))
            update_student(name,grade)
        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Closing The Program...")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
