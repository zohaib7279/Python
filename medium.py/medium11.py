count = str(input("Enter The Sentence = "))
vowel = "aeiouAEIOU"
count.count(vowel)
sum = count.count('a') + count.count('e') + count.count('i') + count.count('o') + count.count('u') + count.count('A') + count.count('E') + count.count('I') + count.count('O') + count.count('U')
print(f"The number of vowels in the sentence is: {sum}")