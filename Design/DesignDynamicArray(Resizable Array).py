class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        array_doubled = [0] * self.capacity

        for i in range(self.length):
            array_doubled[i] = self.array[i]

        self.array = array_doubled

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity


# Test cases
def run_tests():
    # Test 1: Initialization
    da = DynamicArray(2)
    print(f"Test 1 (Init): Size={da.getSize()}, Capacity={da.getCapacity()}")
    # Expected: Size=0, Capacity=2

    # Test 2: Set and Get (within initial capacity)
    da.set(0, 10)
    # Note: 'set' directly modifies the underlying array but doesn't change length.
    # Usually in dynamic arrays, 'set' is valid only for indices < length.
    # However, this implementation allows setting within capacity.
    print(f"Test 2 (Set/Get): get(0)={da.get(0)}")
    # Expected: 10

    # Test 3: Pushback within capacity
    da.pushback(20)  # array[0] becomes 20, overwriting the 10 set manually?
    # No, pushback uses self.length. Init length is 0.
    # So pushback writes to index 0.
    da.pushback(30)  # writes to index 1.
    print(f"Test 3 (Pushback): Size={da.getSize()}, Capacity={da.getCapacity()}")
    print(f"Val at 0: {da.get(0)}, Val at 1: {da.get(1)}")
    # Expected: Size=2, Capacity=2, Vals: 20, 30

    # Test 4: Resize on pushback
    da.pushback(40)  # Capacity is 2, length is 2. Triggers resize.
    print(f"Test 4 (Resize): Size={da.getSize()}, Capacity={da.getCapacity()}")
    print(f"Val at 2: {da.get(2)}")
    # Expected: Size=3, Capacity=4, Val at 2: 40

    # Test 5: Popback
    val = da.popback()
    print(f"Test 5 (Popback): Popped={val}, Size={da.getSize()}")
    # Expected: Popped=40, Size=2

    # Test 6: Get Capacity
    print(f"Test 6 (Capacity): {da.getCapacity()}")
    # Expected: 4 (Capacity usually doesn't shrink on pop)


run_tests()
