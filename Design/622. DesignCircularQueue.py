class MyCircularQueue:
    """
    Circular queue using a fixed-size array.

    Time Complexity:
        enQueue, deQueue, Front, Rear, isEmpty, isFull: O(1)

    Space Complexity:
        O(k) where k is the capacity passed to the constructor.
    """

    def __init__(self, k: int):
        self.array = [0] * k
        self.capacity = k
        self.head_index = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.count:
            return False

        self.array[(self.head_index + self.count) % self.capacity] = value
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.array[self.head_index] if self.count != 0 else -1

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.array[(self.head_index + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Test cases
def test_circular_queue():
    # Test case 1: Basic operations (from LeetCode example)
    print("=== Test Case 1: Basic Operations ===")
    cq = MyCircularQueue(3)

    print(f"Initial: isEmpty={cq.isEmpty()}, isFull={cq.isFull()}")

    res1 = cq.enQueue(1)
    print(f"enQueue(1): {res1}")

    res2 = cq.enQueue(2)
    print(f"enQueue(2): {res2}")

    res3 = cq.enQueue(3)
    print(f"enQueue(3): {res3}")

    print(f"Front: {cq.Front()}, Rear: {cq.Rear()}")
    print(f"isEmpty: {cq.isEmpty()}, isFull: {cq.isFull()}")

    res4 = cq.enQueue(4)  # Should fail - full
    print(f"enQueue(4) when full: {res4}")

    res5 = cq.deQueue()
    print(f"deQueue(): {res5}")
    print(f"Front: {cq.Front()}, Rear: {cq.Rear()}")

    res6 = cq.deQueue()
    print(f"deQueue(): {res6}")
    print(f"Front: {cq.Front()}, Rear: {cq.Rear()}")

    # Test case 2: Wrap-around behavior
    print("\n=== Test Case 2: Wrap-around ===")
    cq2 = MyCircularQueue(3)
    cq2.enQueue(10)
    cq2.enQueue(20)
    cq2.deQueue()  # Remove 10
    cq2.deQueue()  # Remove 20
    cq2.enQueue(30)
    cq2.enQueue(40)
    print(f"After wrap-around - Front: {cq2.Front()}, Rear: {cq2.Rear()}")

    # Test case 3: Empty queue operations
    print("\n=== Test Case 3: Empty Queue ===")
    cq3 = MyCircularQueue(2)
    print(f"Empty - Front: {cq3.Front()}, Rear: {cq3.Rear()}")
    print(f"deQueue on empty: {cq3.deQueue()}")

    # Test case 4: Full queue edge case
    print("\n=== Test Case 4: Full Queue ===")
    cq4 = MyCircularQueue(1)
    cq4.enQueue(100)
    print(f"Full queue enQueue: {cq4.enQueue(200)}")


test_circular_queue()
