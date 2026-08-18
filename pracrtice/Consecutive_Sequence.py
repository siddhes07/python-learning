def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Start counting only if num is the beginning
        # of a consecutive sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


nums = list(map(int, input("Enter numbers: ").split()))

result = longest_consecutive(nums)

print("Longest consecutive sequence length:", result)