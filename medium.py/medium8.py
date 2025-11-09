def is_palindrome(word):
    return word == word[::-1]
words = ["python", "Html", "Css"]    

for w in words:
    if is_palindrome(w):
        print(f"{w} is a palindrome")
    else:
        print(f"{w} is not a palindrome")