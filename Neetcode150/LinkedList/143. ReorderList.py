# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head

        # Find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        middle = slow
        prev = None
        while middle:
            _next = middle.next
            middle.next = prev
            prev = middle
            middle = _next

        # Merge two halves
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp
            

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
head1 = create_linked_list([1, 2, 3, 4])
solution.reorderList(head1)
print(f"Test case 1: {linked_list_to_array(head1)}")  # Expected: [1, 4, 2, 3]

# Test case 2
head2 = create_linked_list([1, 2, 3, 4, 5])
solution.reorderList(head2)
print(f"Test case 2: {linked_list_to_array(head2)}")  # Expected: [1, 5, 2, 4, 3]

# Test case 3
head3 = create_linked_list([1, 2])
solution.reorderList(head3)
print(f"Test case 3: {linked_list_to_array(head3)}")  # Expected: [1, 2]

# Test case 4
head4 = create_linked_list([1])
solution.reorderList(head4)
print(f"Test case 4: {linked_list_to_array(head4)}")  # Expected: [1]

# Test case 5
head5 = create_linked_list([1, 2, 3])
solution.reorderList(head5)
print(f"Test case 5: {linked_list_to_array(head5)}")  # Expected: [1, 3, 2]

# Test case 6
head6 = create_linked_list([1, 2, 3, 4, 5, 6])
solution.reorderList(head6)
print(f"Test case 6: {linked_list_to_array(head6)}")  # Expected: [1, 6, 2, 5, 3, 4]
