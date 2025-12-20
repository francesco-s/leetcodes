class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        curr = self.head.next

        while curr and i < index:
            curr = curr.next
            i += 1

        if not curr:
            return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        old_head = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = old_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        i = 0
        curr = self.head

        while i < index:
            curr = curr.next
            i += 1

        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        i = 0
        curr = self.head

        while i < index:
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Test cases
obj = MyLinkedList()

# Test case 1 (Example from LeetCode)
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]

obj.addAtHead(1)
print("Added head 1. List: 1")

obj.addAtTail(3)
print("Added tail 3. List: 1->3")

obj.addAtIndex(1, 2)
print("Added 2 at index 1. List: 1->2->3")

res1 = obj.get(1)
print(f"Get index 1: {res1}")  # Expected: 2

obj.deleteAtIndex(1)
print("Deleted index 1. List: 1->3")

res2 = obj.get(1)
print(f"Get index 1: {res2}")  # Expected: 3

# Test case 2 (Invalid index operations)
obj2 = MyLinkedList()
obj2.addAtHead(10)
res3 = obj2.get(1)
print(f"Test case 2 - Invalid get: {res3}")  # Expected: -1

obj2.addAtIndex(5, 50)  # Should do nothing
print(f"Test case 2 - Add at invalid index. Size: {obj2.size}")  # Expected size: 1

obj2.deleteAtIndex(5)  # Should do nothing
print(f"Test case 2 - Delete at invalid index. Size: {obj2.size}")  # Expected size: 1
