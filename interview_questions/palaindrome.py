def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word = input("Enter a word/number: ")
if is_palindrome(word):
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is NOT a Palindrome")