# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.
        Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2.
        Space Complexity: O(max(N, M)), for the output linked list.
        """
        res = ListNode(0) 
        dummy = res
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            _sum = val1 + val2 + carry
            carry = _sum // 10

            res.next = ListNode(_sum % 10)
            res = res.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbersLong(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists (alternative implementation).
        Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2.
        Space Complexity: O(max(N, M)), for the output linked list.
        """
        curr1 = l1
        curr2 = l2

        res = ListNode(0)
        dummy = res

        to_add = 0

        while curr1 and curr2:
            _sum = curr1.val + curr2.val + to_add
            res.next = ListNode(_sum % 10)

            if _sum // 10 == 1:
                to_add = 1
            else:
                to_add = 0

            curr1 = curr1.next
            curr2 = curr2.next
            res = res.next

        while curr1:
            _sum = curr1.val + to_add
            res.next = ListNode(_sum % 10)

            if _sum // 10 == 1:
                to_add = 1
            else:
                to_add = 0
            curr1 = curr1.next
            res = res.next
        while curr2:
            _sum = curr2.val + to_add
            res.next = ListNode(_sum % 10)

            if _sum // 10 == 1:
                to_add = 1
            else:
                to_add = 0
            curr2 = curr2.next
            res = res.next

        if to_add == 1:
            res.next = ListNode(1)

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
l1_1 = create_linked_list([2, 4, 3])
l2_1 = create_linked_list([5, 6, 4])
result1 = solution.addTwoNumbers(l1_1, l2_1)
print(f"Test case 1: {linked_list_to_array(result1)}")  # Expected: [7, 0, 8]

# Test case 2
l1_2 = create_linked_list([0])
l2_2 = create_linked_list([0])
result2 = solution.addTwoNumbers(l1_2, l2_2)
print(f"Test case 2: {linked_list_to_array(result2)}")  # Expected: [0]

# Test case 3
l1_3 = create_linked_list([9,9,9,9,9,9,9])
l2_3 = create_linked_list([9,9,9,9])
result3 = solution.addTwoNumbers(l1_3, l2_3)
print(f"Test case 3: {linked_list_to_array(result3)}")  # Expected: [8,9,9,9,0,0,0,1]

# Test case 4
l1_4 = create_linked_list([1])
l2_4 = create_linked_list([9,9,9])
result4 = solution.addTwoNumbers(l1_4, l2_4)
print(f"Test case 4: {linked_list_to_array(result4)}")  # Expected: [0,0,0,1]

# Test case 5
l1_5 = create_linked_list([5,6])
l2_5 = create_linked_list([5,6])
result5 = solution.addTwoNumbers(l1_5, l2_5)
print(f"Test case 5: {linked_list_to_array(result5)}")  # Expected: [0,3,1]

# Test case 6
l1_6 = create_linked_list([0])
l2_6 = create_linked_list([7,3])
result6 = solution.addTwoNumbers(l1_6, l2_6)
print(f"Test case 6: {linked_list_to_array(result6)}")  # Expected: [7,3]
