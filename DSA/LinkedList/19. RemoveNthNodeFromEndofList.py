# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Placeholder for the solution implementation
        dummy = ListNode(0, head)
        slow = fast = dummy
        i = 0

        while i < n + 1 and fast:
            fast = fast.next
            i += 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
solution = Solution()

# Test case 1
head1 = create_linked_list([1, 2, 3, 4, 5])
result1 = solution.removeNthFromEnd(head1, 2)
print(f"Test case 1: {linked_list_to_list(result1)}")  # Expected: [1, 2, 3, 5]

# Test case 2
head2 = create_linked_list([1])
result2 = solution.removeNthFromEnd(head2, 1)
print(f"Test case 2: {linked_list_to_list(result2)}")  # Expected: []

# Test case 3
head3 = create_linked_list([1, 2])
result3 = solution.removeNthFromEnd(head3, 1)
print(f"Test case 3: {linked_list_to_list(result3)}")  # Expected: [1]

# Test case 4
head4 = create_linked_list([1, 2, 3])
result4 = solution.removeNthFromEnd(head4, 1)
print(f"Test case 4: {linked_list_to_list(result4)}")  # Expected: [1, 2]