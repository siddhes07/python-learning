a = [1,2,3,2,1]
b = [1,2,6,2,1] 

copy_a = a.copy()
copy_a.reverse()

if copy_a == b:
    print("List is palindrome")
else:
    print("List is not palindrome")