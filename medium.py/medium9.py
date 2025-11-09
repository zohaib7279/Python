def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

while True:
    try:
        f = float(input("Enter temperature in Fahrenheit: "))
        convert_to_celsius(f)
        break
    except ValueError:
        print("Please enter a valid number")
