# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Placeholder for the solution
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        return res == res[::-1]

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
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
values1 = [1, 2, 2, 1]
head1 = create_linked_list(values1)
result1 = solution.isPalindrome(head1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
values2 = [1, 2]
head2 = create_linked_list(values2)
result2 = solution.isPalindrome(head2)
print(f"Test case 2: {result2}")  # Expected: False

# Test case 3
values3 = [1]
head3 = create_linked_list(values3)
result3 = solution.isPalindrome(head3)
print(f"Test case 3: {result3}")  # Expected: True

# Test case 4
values4 = []
head4 = create_linked_list(values4)
result4 = solution.isPalindrome(head4)
print(f"Test case 4: {result4}")  # Expected: True