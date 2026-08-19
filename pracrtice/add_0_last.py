arr = [ 1, 0 , 2 ,3 ,0 ,4 ,5]

result = []

for i in arr:
    if i !=0:
        result.append(i)

for i in arr:
    if i == 0:
        result.append(i)

print(result)