num = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
sum = num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9]
average = sum / len(num)
lar_small = max(num) - min(num)
print(f"Sum = {sum} , average = {average} , largest - smallest = {lar_small}")