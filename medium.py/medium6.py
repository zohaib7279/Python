# step 1: start
# step 2: create list of even numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 3: create empty list to store even numbers
even_numbers = []
# step 4: loop through the numbers and check if they are even
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
# step 5: print the list of even numbers
print("Even numbers list:", even_numbers)
# step 6: end