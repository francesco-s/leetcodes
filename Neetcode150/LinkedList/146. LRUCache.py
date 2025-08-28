class ListNode:
    def __init__(self, key, val, prev = None, _next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = _next


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove(node)
        self.add(node)

        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            old_node = self.dict[key]
            self.remove(old_node)

        new_node = ListNode(key, value)
        self.dict[key] = new_node
        self.add(new_node)

        if len(self.dict) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]
        

    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

# Test cases

# Test case 1
lRUCache1 = LRUCache(2)
lRUCache1.put(1, 1)
lRUCache1.put(2, 2)
result1_1 = lRUCache1.get(1)
print(f"Test case 1.1: {result1_1}")  # Expected: 1

lRUCache1.put(3, 3)  # evicts key 2
result1_2 = lRUCache1.get(2)
print(f"Test case 1.2: {result1_2}")  # Expected: -1

lRUCache1.put(4, 4)  # evicts key 1
result1_3 = lRUCache1.get(1)
print(f"Test case 1.3: {result1_3}")  # Expected: -1

result1_4 = lRUCache1.get(3)
print(f"Test case 1.4: {result1_4}")  # Expected: 3

result1_5 = lRUCache1.get(4)
print(f"Test case 1.5: {result1_5}")  # Expected: 4

# Test case 2 - Capacity 1
lRUCache2 = LRUCache(1)
lRUCache2.put(2, 1)
result2_1 = lRUCache2.get(2)
print(f"Test case 2.1: {result2_1}")  # Expected: 1

lRUCache2.put(3, 2)  # evicts key 2
result2_2 = lRUCache2.get(2)
print(f"Test case 2.2: {result2_2}")  # Expected: -1

result2_3 = lRUCache2.get(3)
print(f"Test case 2.3: {result2_3}")  # Expected: 2

# Test case 3 - Update existing key
lRUCache3 = LRUCache(2)
lRUCache3.put(1, 1)
lRUCache3.put(2, 2)
lRUCache3.put(1, 10)  # update key 1
result3_1 = lRUCache3.get(1)
print(f"Test case 3.1: {result3_1}")  # Expected: 10

result3_2 = lRUCache3.get(2)
print(f"Test case 3.2: {result3_2}")  # Expected: 2
