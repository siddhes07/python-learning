
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy

    for num in numbers:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print("Output:", "[" + ",".join(result) + "]")


# Take input from the user
num1 = list(map(int, input("Enter digits of first number (comma-separated): ").split(",")))
num2 = list(map(int, input("Enter digits of second number (comma-separated): ").split(",")))

l1 = create_linked_list(num1)
l2 = create_linked_list(num2)

result = addTwoNumbers(l1, l2)

print_linked_list(result)
