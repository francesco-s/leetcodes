from typing import Optional


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
# Example 2:
#
# Input: head = [5], left = 1, right = 1
# Output: [5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween2(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        to_invert = []

        while current:
            to_invert.append(current.val)
            current = current.next

        to_invert[left - 1:right] = to_invert[left - 1:right][::-1]
        print(to_invert)
        return create_linked_list(to_invert)

    def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head

        current = head
        prev, left_node = None, None

        i = 1

        while current and i < left:
            left_node = current
            current = current.next
            i += 1

        first_swap_node = current

        while current and i <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        if left_node:
            left_node.next = prev

        if current and left == 1:
            first_swap_node.next = current
            head = prev
        elif current:
            first_swap_node.next = current
        elif not left_node:
            head = prev

        return head


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
        # print(node.val)
        lst.append(node.val)
        node = node.next
    return lst


l1 = create_linked_list([1, 2, 3, 4, 5])
l2 = create_linked_list([5])
l3 = create_linked_list([0, 1, 2, 3, 4, 5, 6])
l4 = create_linked_list([3, 5])
l5 = create_linked_list([3, 5])
l6 = create_linked_list([1, 2, 3])
l7 = create_linked_list([1, 2, 3])

print(linked_list_to_list(Solution.reverseBetween(l1, left=2, right=4)))
print(linked_list_to_list(Solution.reverseBetween(l2, left=1, right=1)))
print(linked_list_to_list(Solution.reverseBetween(l3, left=3, right=5)))
print(linked_list_to_list(Solution.reverseBetween(l4, left=1, right=2)))
print(linked_list_to_list(Solution.reverseBetween(l5, left=2, right=2)))
print(linked_list_to_list(Solution.reverseBetween(l6, left=1, right=2)))
print(linked_list_to_list(Solution.reverseBetween(l7, left=2, right=3)))
