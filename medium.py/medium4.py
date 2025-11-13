# step 1: start
# step 2: create a list of numbers and calculate sum, average, largest - smallest 
num = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# step 3: calculate sum
sum = num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9]
# step 4: calculate average
average = sum / len(num)
# step 5: calculate largest - smallest
lar_small = max(num) - min(num)
# step 6: print sum, average, largest - smallest
print(f"Sum = {sum} , average = {average} , largest - smallest = {lar_small}")