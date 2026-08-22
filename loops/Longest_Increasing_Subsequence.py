arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

n = len(arr)

length = [1] * n
previous = [-1] * n

for i in range(n):

    for j in range(i):

        if arr[j] < arr[i]:

            if length[j] + 1 > length[i]:

                length[i] = length[j] + 1
                previous[i] = j


# Find maximum length manually
max_length = 0
max_index = 0

for i in range(n):

    if length[i] > max_length:
        max_length = length[i]
        max_index = i


# Reconstruct subsequence
result = []

index = max_index

while index != -1:

    result.append(arr[index])

    index = previous[index]


# Reverse manually using loop
final_result = []

i = len(result) - 1

while i >= 0:

    final_result.append(result[i])

    i -= 1


print("Longest subsequence:", final_result)
print("Length:", max_length)