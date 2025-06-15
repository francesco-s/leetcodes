# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Placeholder for the solution implementation
        prehead = ListNode(-1)

        prev = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 is not None else list2

        return prehead.next

        
        return create_linked_list(res)
    def mergeTwoListsBad(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Placeholder for the solution implementation
        res = []
        while list1 and list2:
            if list1.val < list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next

        while list1:
            res.append(list1.val)
            list1 = list1.next
        
        while list2:
            res.append(list2.val)
            list2 = list2.next
        
        return create_linked_list(res)


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
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
solution = Solution()

# Test case 1
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged = solution.mergeTwoLists(list1, list2)
print(f"Test case 1: {linked_list_to_list(merged)}")  # Expected: [1, 1, 2, 3, 4, 4]

# Test case 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged = solution.mergeTwoLists(list1, list2)
print(f"Test case 2: {linked_list_to_list(merged)}")  # Expected: []

# Test case 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged = solution.mergeTwoLists(list1, list2)
print(f"Test case 3: {linked_list_to_list(merged)}")  # Expected: [0]