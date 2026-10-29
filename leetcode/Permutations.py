
from itertools import permutations

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = list(permutations(nums))

result = [list(p) for p in result]

print("All permutations:")
print(result)
