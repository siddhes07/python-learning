arr = [10, 45, 20, 45, 30, 50, 50, 40]

largest = None
second_largest = None

for i in range(len(arr)):

    current = arr[i]

    # Check whether current number appeared before
    duplicate = False

    for j in range(i):
        if arr[j] == current:
            duplicate = True
            break

    if duplicate:
        continue

    if largest is None or current > largest:

        second_largest = largest
        largest = current

    elif current != largest and (
        second_largest is None or current > second_largest
    ):

        second_largest = current


print("Largest:", largest)
print("Second largest:", second_largest)