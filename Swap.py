class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # Swap
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to next pair
        prev = first

    return dummy.next


# Take input from user
values = list(map(int, input("Enter elements: ").split()))

# Create linked list
head = None
tail = None

for value in values:
    new_node = ListNode(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

# Swap nodes
head = swapPairs(head)

# Print result
current = head

while current:
    print(current.val, end=" ")
    current = current.next
