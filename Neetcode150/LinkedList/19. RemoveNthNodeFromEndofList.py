# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the linked list and returns its head.

        Time Complexity: O(L), where L is the length of the linked list (two passes).
        Space Complexity: O(1), only constant extra space is used.
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = head

        n_el = 0

        while curr:
            n_el += 1
            curr = curr.next

        curr = dummy
        n_el -= n
        while n_el > 0:
            n_el -= 1
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next

# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to convert linked list to array for printing
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
solution = Solution()

# Test case 1
head1 = create_linked_list([1, 2, 3, 4, 5])
n1 = 2
result1 = solution.removeNthFromEnd(head1, n1)
print(f"Test case 1: {linked_list_to_array(result1)}")  # Expected: [1, 2, 3, 5]

# Test case 2
head2 = create_linked_list([1])
n2 = 1
result2 = solution.removeNthFromEnd(head2, n2)
print(f"Test case 2: {linked_list_to_array(result2)}")  # Expected: []

# Test case 3
head3 = create_linked_list([1, 2])
n3 = 1
result3 = solution.removeNthFromEnd(head3, n3)
print(f"Test case 3: {linked_list_to_array(result3)}")  # Expected: [1]

# Test case 4
head4 = create_linked_list([1, 2])
n4 = 2
result4 = solution.removeNthFromEnd(head4, n4)
print(f"Test case 4: {linked_list_to_array(result4)}")  # Expected: [2]

# Test case 5
head5 = create_linked_list([1, 2, 3, 4, 5])
n5 = 1
result5 = solution.removeNthFromEnd(head5, n5)
print(f"Test case 5: {linked_list_to_array(result5)}")  # Expected: [1, 2, 3, 4]

# Test case 6
head6 = create_linked_list([1, 2, 3, 4, 5])
n6 = 5
result6 = solution.removeNthFromEnd(head6, n6)
print(f"Test case 6: {linked_list_to_array(result6)}")  # Expected: [2, 3, 4, 5]
