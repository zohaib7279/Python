vowels1 = input("Enter first name = ")
vowels2 = input("Enter second name = ")
vowels3 = input("Enter third name = ")
vowels4 = input("Enter forth name = ")
vowels5 = input("Enter fifth name = ")

store = [vowels1, vowels2, vowels3, vowels4, vowels5]

for name in store:
    if name[0] in 'aeiouAEIOU':
        print(f"{name} starts with a vowel")
