text = input("enter a number : ")

if text == text[::-1]:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")