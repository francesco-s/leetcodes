class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Placeholder for the solution
        curr = head
        seen = set()

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

# Helper function to create a linked list from a list of values
def create_linked_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]  # Create a cycle
    return nodes[0]

# Test cases
solution = Solution()

# Test case 1: No cycle
values1 = [3, 2, 0, -4]
pos1 = -1  # No cycle
head1 = create_linked_list(values1, pos1)
print(f"Test case 1: {solution.hasCycle(head1)}")  # Expected: False

# Test case 2: Cycle exists
values2 = [1, 2]
pos2 = 0  # Cycle back to the first node
head2 = create_linked_list(values2, pos2)
print(f"Test case 2: {solution.hasCycle(head2)}")  # Expected: True

# Test case 3: Single node, no cycle
values3 = [1]
pos3 = -1  # No cycle
head3 = create_linked_list(values3, pos3)
print(f"Test case 3: {solution.hasCycle(head3)}")  # Expected: False

# Test case 4: Single node, cycle exists
values4 = [1]
pos4 = 0  # Cycle back to itself
head4 = create_linked_list(values4, pos4)
print(f"Test case 4: {solution.hasCycle(head4)}")  # Expected: True