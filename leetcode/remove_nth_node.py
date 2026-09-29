class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# User input
nums = list(map(int, input("Enter linked list elements: ").split()))
n = int(input("Enter n: "))


# Create linked list
dummy = ListNode(0)
current = dummy

for num in nums:
    current.next = ListNode(num)
    current = current.next


# Remove Nth node from end
head = dummy.next

dummy = ListNode(0)
dummy.next = head

slow = dummy
fast = dummy

for _ in range(n):
    fast = fast.next

while fast.next:
    slow = slow.next
    fast = fast.next

slow.next = slow.next.next

head = dummy.next


# Print result
current = head

while current:
    print(current.val, end=" ")
    current = current.next