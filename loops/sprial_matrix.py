n = int(input("Enter n: "))

matrix = [[0 for _ in range(n)] for _ in range(n)]

num = 2
top = 0
bottom = n - 1
left = 0
right = n - 1


def is_prime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


while top <= bottom and left <= right:

    # Left → Right
    for col in range(left, right + 1):
        if is_prime(num):
            matrix[top][col] = num
        num += 1
    top += 1

    # Top → Bottom
    for row in range(top, bottom + 1):
        if is_prime(num):
            matrix[row][right] = num
        num += 1
    right -= 1

    # Right → Left
    if top <= bottom:
        for col in range(right, left - 1, -1):
            if is_prime(num):
                matrix[bottom][col] = num
            num += 1
        bottom -= 1

    # Bottom → Top
    if left <= right:
        for row in range(bottom, top - 1, -1):
            if is_prime(num):
                matrix[row][left] = num
            num += 1
        left += 1


for row in matrix:
    for value in row:
        print(f"{value:3}", end=" ")
    print()