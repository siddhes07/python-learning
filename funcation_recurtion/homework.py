'''
Write a function that takes a number as input.
If the number is even, return "Even".
If the number is odd, return "Odd".
'''

num = int(input("Enter a number: "))

def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_even(num))