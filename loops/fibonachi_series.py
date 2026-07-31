input = int ( input("Enter the number of terms: "))
a, b = 0, 1

for i in range(input):
    print(a, end=" ")
    c = a + b
    a = b
    b = c