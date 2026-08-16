s = input("Enter a string: ")

frequency = {}

# Count frequency
for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Find first non-repeating character
for ch in s:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break