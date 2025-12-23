class MyCircularDeque:
    def __init__(self, k: int):
        # TC: O(k), SC: O(k)
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        # TC: O(1), SC: O(1)
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        # TC: O(1), SC: O(1)
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        # TC: O(1), SC: O(1)
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # TC: O(1), SC: O(1)
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        # TC: O(1), SC: O(1)
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        # TC: O(1), SC: O(1)
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        # TC: O(1), SC: O(1)
        return self.size == 0

    def isFull(self) -> bool:
        # TC: O(1), SC: O(1)
        return self.size == self.capacity


# Test cases
def test_circular_deque():
    print("=== Test Case 1: Basic Operations (capacity=3) ===")
    deq = MyCircularDeque(3)

    print(f"Initial: Empty={deq.isEmpty()}, Full={deq.isFull()}")

    # Fill deque
    print(f"insertFront(1): {deq.insertFront(1)}")
    print(f"insertLast(2): {deq.insertLast(2)}")
    print(f"insertLast(3): {deq.insertLast(3)}")
    print(f"Front: {deq.getFront()}, Rear: {deq.getRear()}")

    # Full check
    print(f"insertLast(4) when full: {deq.insertLast(4)}")

    # Delete operations
    print(f"deleteFront(): {deq.deleteFront()}")
    print(f"Front: {deq.getFront()}, Rear: {deq.getRear()}")

    print(f"insertFront(4): {deq.insertFront(4)}")
    print(f"Front: {deq.getFront()}, Rear: {deq.getRear()}")

    print("\n=== Test Case 2: Wrap-around Behavior (capacity=3) ===")
    deq2 = MyCircularDeque(3)
    deq2.insertLast(10)
    deq2.insertLast(20)
    deq2.deleteFront()  # Remove 10
    deq2.insertLast(30)  # Should go to front position
    print(f"After wrap - Front: {deq2.getFront()}, Rear: {deq2.getRear()}")

    print("\n=== Test Case 3: Edge Cases ===")
    deq3 = MyCircularDeque(1)
    print(f"Empty getFront: {deq3.getFront()}")
    print(f"Empty getRear: {deq3.getRear()}")

    deq3.insertLast(100)
    print(f"Single element - Front: {deq3.getFront()}, Rear: {deq3.getRear()}")

    deq3.deleteLast()
    print(f"deleteLast on single: {deq3.deleteLast()}")  # Should return False
    print(f"Empty after delete: {deq3.isEmpty()}")


test_circular_deque()
