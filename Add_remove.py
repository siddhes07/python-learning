# List program

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original List:", numbers)

# Add an element
x = int(input("Enter number to add: "))
numbers.append(x)

print("After adding:", numbers)

# Remove an element
x = int(input("Enter number to remove: "))

if x in numbers:
    numbers.remove(x)
    print("After removing:", numbers)
else:
    print("Number not found")

# Search an element
x = int(input("Enter number to search: "))

if x in numbers:
    print("Number is present in the list")
else:
    print("Number is not present")
