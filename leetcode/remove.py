def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# User input
nums = list(map(int, input("Enter array elements: ").split()))
val = int(input("Enter value to remove: "))

k = removeElement(nums, val)

print("Number of remaining elements:", k)
print("Array after removing:", nums[:k])