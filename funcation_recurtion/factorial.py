n = int(input("Enter a number: "))

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(cal_fact(n))
