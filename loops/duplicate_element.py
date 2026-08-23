arr = [10, 20, 30, 20, 40, 10, 50, 30]

duplicates = []

for i in range(len(arr)):

    for j in range(i + 1, len(arr)):

        if arr[i] == arr[j]:

            already_exists = False

            for k in range(len(duplicates)):
                if duplicates[k] == arr[i]:
                    already_exists = True

            if not already_exists:
                duplicates.append(arr[i])

print("Duplicates:", duplicates)