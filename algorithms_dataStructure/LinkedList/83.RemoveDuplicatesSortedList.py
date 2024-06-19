from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head

        res = ListNode()
        current = res

        while actual:
            current.next = ListNode(actual.val)
            current = current.next
            while actual and actual.next and actual.val == actual.next.val:
                actual = actual.next
            actual = actual.next

        return res.next



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


l1 = create_linked_list([1, 1, 2])
l2 = create_linked_list([1, 1, 2, 3, 3])

print(linked_list_to_list(Solution.deleteDuplicates(l1)))
print(linked_list_to_list(Solution.deleteDuplicates(l2)))
