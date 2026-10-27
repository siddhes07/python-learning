def two_sum(nums, target):
    seen = {}                      # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []                      # no answer found

nums = list(map(int, input("Enter numbers (space separated): ").split()))
target = int(input("Enter target: "))

print("Indices:", two_sum(nums, target))