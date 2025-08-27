# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n + m), where n and m are the lengths of list1 and list2.
    # Space Complexity: O(1) for mergeTwoListsOptimal (in-place), O(n + m) for mergeTwoLists (new nodes).
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
    
        return dummy.next

    # Time Complexity: O(n + m), where n and m are the lengths of list1 and list2.
    # Space Complexity: O(n + m), since new nodes are created for the merged list.
    def mergeTwoListsBad(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        if curr1.val < curr2.val:
            new_head = ListNode(curr1.val)
            curr1 = curr1.next
        else:
            new_head = ListNode(curr2.val)
            curr2 = curr2.next

        curr3 = new_head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next
            
            curr3 = curr3.next
        
        if curr1:
            curr3.next = curr1
        else:
            curr3.next = curr2

        return new_head

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
list1_1 = create_linked_list([1, 2, 4])
list2_1 = create_linked_list([1, 3, 4])
result1 = solution.mergeTwoLists(list1_1, list2_1)
print(f"Test case 1: {linked_list_to_array(result1)}")  # Expected: [1, 1, 2, 3, 4, 4]

# Test case 2
list1_2 = create_linked_list([])
list2_2 = create_linked_list([])
result2 = solution.mergeTwoLists(list1_2, list2_2)
print(f"Test case 2: {linked_list_to_array(result2)}")  # Expected: []

# Test case 3
list1_3 = create_linked_list([])
list2_3 = create_linked_list([0])
result3 = solution.mergeTwoLists(list1_3, list2_3)
print(f"Test case 3: {linked_list_to_array(result3)}")  # Expected: [0]

# Test case 4
list1_4 = create_linked_list([2])
list2_4 = create_linked_list([1])
result4 = solution.mergeTwoLists(list1_4, list2_4)
print(f"Test case 4: {linked_list_to_array(result4)}")  # Expected: [1, 2]

# Test case 5
list1_5 = create_linked_list([1, 3, 5])
list2_5 = create_linked_list([2, 4, 6])
result5 = solution.mergeTwoLists(list1_5, list2_5)
print(f"Test case 5: {linked_list_to_array(result5)}")  # Expected: [1, 2, 3, 4, 5, 6]
