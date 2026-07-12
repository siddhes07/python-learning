numbers = [10, 20, 30, 40, 50]

last = numbers[-1]
numbers.pop()
numbers.insert(0, last)

print("Rotated List:", numbers)