def searchRange(nums, target):
    first = -1
    last = -1

    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i

    return [first, last]


# Take input from user
nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

result = searchRange(nums, target)

print("Output:", result)