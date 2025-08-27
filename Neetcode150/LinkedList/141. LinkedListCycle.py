# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list has a cycle.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1), uses constant extra space.
        """
        if not head:
            return False
        
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Helper function to create a linked list with a cycle
def create_cycle_list(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

# Test cases
solution = Solution()

# Test case 1
head1 = create_cycle_list([3, 2, 0, -4], 1)
result1 = solution.hasCycle(head1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
head2 = create_cycle_list([1, 2], 0)
result2 = solution.hasCycle(head2)
print(f"Test case 2: {result2}")  # Expected: True

# Test case 3
head3 = create_cycle_list([1], -1)
result3 = solution.hasCycle(head3)
print(f"Test case 3: {result3}")  # Expected: False

# Test case 4
head4 = create_cycle_list([1, 2, 3, 4, 5], 2)
result4 = solution.hasCycle(head4)
print(f"Test case 4: {result4}")  # Expected: True

# Test case 5
head5 = create_cycle_list([1, 2, 3, 4, 5], -1)
result5 = solution.hasCycle(head5)
print(f"Test case 5: {result5}")  # Expected: False

# Test case 6
head6 = None
result6 = solution.hasCycle(head6)
print(f"Test case 6: {result6}")  # Expected: False
