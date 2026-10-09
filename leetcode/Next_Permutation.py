
def nextPermutation(nums):
    n = len(nums)

    # Step 1: Find the first decreasing element from right
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find the next greater element from right
    if i >= 0:
        j = n - 1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the remaining elements
    nums[i + 1:] = reversed(nums[i + 1:])


# Take input from user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

nextPermutation(nums)

print("Next permutation:", nums)
