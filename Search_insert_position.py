def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Take input from the user
nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

result = searchInsert(nums, target)
print("Insert position:", result)
