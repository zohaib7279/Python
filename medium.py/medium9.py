from fractions import Fraction
def convert_to_celsius(fahrenheit):
    # (F - 32) * 5/9 are the formula to convert Fahrenheit to Celsius
    celsius = (int(fahrenheit) - 32) * Fraction(5, 9)
    return celsius
print(convert_to_celsius(int(input("Enter The number convert to Celsius = "))))
    