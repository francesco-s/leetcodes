# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Dummy node to start the new list
    dummy = ListNode()
    current = dummy
    carry = 0

    # Loop until both lists are exhausted and there's no carry left
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        new_val = total % 10

        current.next = ListNode(new_val)
        current = current.next

        # Move to the next nodes in the lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
print(linked_list_to_list((addTwoNumbers(l1, l2))))

l1 = create_linked_list([0])
l2 = create_linked_list([0])
print(linked_list_to_list((addTwoNumbers(l1, l2))))

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
print(linked_list_to_list((addTwoNumbers(l1, l2))))
