a = [10, 20, 30, 40, 50]
b = [20, 30, 60, 40]
c = [30, 40, 70, 20]

common = []

for i in range(len(a)):

    found_in_b = False
    found_in_c = False

    for j in range(len(b)):
        if a[i] == b[j]:
            found_in_b = True
            break

    for k in range(len(c)):
        if a[i] == c[k]:
            found_in_c = True
            break

    if found_in_b and found_in_c:
        common.append(a[i])

print("Common elements:", common)