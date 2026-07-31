start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):      # Outer loop
    if num > 1:                        # If block
        is_prime = True

        for i in range(2, num):        # Inner loop
            if num % i == 0:           # If block
                is_prime = False
                break

        if is_prime:                   # <-- हा कुठे आहे?
            print(num, end=" ")