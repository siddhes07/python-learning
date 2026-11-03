def findMedianSortedArrays(nums1, nums2):
    arr = sorted(nums1 + nums2)

    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2


# Taking input from user
nums1 = list(map(int, input("Enter first sorted array: ").split()))
nums2 = list(map(int, input("Enter second sorted array: ").split()))

result = findMedianSortedArrays(nums1, nums2)

print("Median:", result)