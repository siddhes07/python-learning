numbers = (2, 5, 2, 8, 5, 2, 9, 8, 5)

visited = ()

for num in numbers:
    if num not in visited:
        count = 0
        for item in numbers:
            if item == num:
                count += 1

        print(f"{num} appears {count} times")
        visited = visited + (num,)