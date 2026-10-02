import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    # First node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        value, i, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# Take input from user
k = int(input("Enter number of linked lists: "))

lists = []

for i in range(k):
    values = list(map(int, input(
        f"Enter elements of list {i + 1} separated by space: "
    ).split()))

    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    lists.append(dummy.next)


# Merge all lists
result = mergeKLists(lists)

# Print result
print("Merged list:", end=" ")

while result:
    print(result.val, end=" ")
    result = result.next