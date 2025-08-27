# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1), since we use only a constant amount of extra space.
        """
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

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
result1 = solution.reverseList(head1)
print(f"Test case 1: {linked_list_to_array(result1)}")  # Expected: [5, 4, 3, 2, 1]

# Test case 2
head2 = create_linked_list([1, 2])
result2 = solution.reverseList(head2)
print(f"Test case 2: {linked_list_to_array(result2)}")  # Expected: [2, 1]

# Test case 3
head3 = create_linked_list([])
result3 = solution.reverseList(head3)
print(f"Test case 3: {linked_list_to_array(result3)}")  # Expected: []

# Test case 4
head4 = create_linked_list([1])
result4 = solution.reverseList(head4)
print(f"Test case 4: {linked_list_to_array(result4)}")  # Expected: [1]

# Test case 5
head5 = create_linked_list([1, 2, 3])
result5 = solution.reverseList(head5)
print(f"Test case 5: {linked_list_to_array(result5)}")  # Expected: [3, 2, 1]
