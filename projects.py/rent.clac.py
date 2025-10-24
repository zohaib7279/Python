rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food orderd ="))
elec_spend = int(input("Enter the total of electricity spend = "))
charge = int(input("Enter the charge per unit = "))
persons = int(input("Enter the person of living in room/flat = "))
total_bill = elec_spend * charge
output = (rent + food + total_bill) // persons
print("Each person will pay = ", output)