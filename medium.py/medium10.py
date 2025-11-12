students = {
    "Arslan :": "75",
    "Bilal :": "87",
    "Tahoor :": "90",
    "Zaim :": "88",
    "Zohaib :": "96"
}
# Print each student's name along with their marks
for name, marks in students.items():
    print(name, marks)
# Calculate the average marks
total_marks = sum(int(marks) for marks in students.values())
average_marks = total_marks / len(students)
print(f"Average marks of the class = {average_marks}")
# Find the highest marks
highest_marks = max(int(marks) for marks in students.values())
print(f"Highest marks in the class = {highest_marks}")