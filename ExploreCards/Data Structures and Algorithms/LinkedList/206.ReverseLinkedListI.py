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
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
    
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


l1 = create_linked_list([1, 2, 3, 4, 5])
l2 = create_linked_list([5])

print(Solution.reverseList(l1))
print(Solution.reverseList(l2))
