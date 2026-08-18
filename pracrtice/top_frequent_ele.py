from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)

    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]


nums = list(map(int, input("Enter numbers separated by space: ").split()))

k = int(input("Enter k: "))

result = top_k_frequent(nums, k)

print("Top", k, "frequent elements:", result)