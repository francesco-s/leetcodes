# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        # Placeholder for the solution
        node.val = node.next.val
        node.next = node.next.next

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
values1 = [4, 5, 1, 9]
head1 = create_linked_list(values1)
node_to_delete1 = head1.next  # Node with value 5
solution.deleteNode(node_to_delete1)
print(f"Test case 1: {linked_list_to_list(head1)}")  # Expected: [4, 1, 9]

# Test case 2
values2 = [1, 2, 3, 4]
head2 = create_linked_list(values2)
node_to_delete2 = head2.next.next  # Node with value 3
solution.deleteNode(node_to_delete2)
print(f"Test case 2: {linked_list_to_list(head2)}")  # Expected: [1, 2, 4]

# Test case 3
values3 = [0, 1]
head3 = create_linked_list(values3)
node_to_delete3 = head3  # Node with value 0
solution.deleteNode(node_to_delete3)
print(f"Test case 3: {linked_list_to_list(head3)}")  # Expected: [1]