class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    result = []

    # Put all values into one list
    for lst in lists:
        current = lst
        while current:
            result.append(current.val)
            current = current.next

    # Sort all values
    result.sort()

    # Create the final linked list
    dummy = ListNode()
    current = dummy

    for value in result:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# User input
k = int(input("Enter number of linked lists: "))

lists = []

for i in range(k):
    values = list(map(int, input(
        f"Enter sorted values for list {i + 1} separated by space: "
    ).split()))

    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    lists.append(dummy.next)


# Merge
answer = mergeKLists(lists)


# Display result
print("Merged Sorted List:")

current = answer

while current:
    print(current.val, end=" ")
    current = current.next
