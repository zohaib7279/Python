# step 1: start
# step 2: ask the user to input five names
vowels1 = input("Enter first name = ")
vowels2 = input("Enter second name = ")
vowels3 = input("Enter third name = ")
vowels4 = input("Enter forth name = ")
vowels5 = input("Enter fifth name = ")
# step 3: the input names are stored in a list
store = [vowels1, vowels2, vowels3, vowels4, vowels5]
# step 4: create a loop to check if the names start with a vowel
for name in store:
    if name[0] in 'aeiouAEIOU':
        print(f"{name} starts with a vowel")
# step 5: end