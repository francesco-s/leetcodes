from typing import List
from collections import defaultdict


class CountSquares:
    # Time Complexity:
    #   add: O(1)
    #   count: O(N), where N is the number of points added so far
    # Space Complexity:
    #   O(N), for storing points and their counts

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if x == px or y == py:
                continue
            if abs(py - y) == abs(px - x):
                res += self.pts_count[(x, py)] * self.pts_count[(px, y)]
        return res


# Test cases

# Test case 1 (example)
obj1 = DetectSquares()
obj1.add([3, 10])
obj1.add([11, 2])
obj1.add([3, 2])
res1 = obj1.count([11, 10])
print(f"Test case 1: {res1}")  # Expected: 1
res1b = obj1.count([14, 8])
print(f"Test case 1b: {res1b}")  # Expected: 0
obj1.add([11, 2])  # duplicate point
res1c = obj1.count([11, 10])
print(f"Test case 1c: {res1c}")  # Expected: 2

# Test case 2 (no squares possible)
obj2 = DetectSquares()
obj2.add([1, 1])
obj2.add([2, 2])
res2 = obj2.count([3, 3])
print(f"Test case 2: {res2}")  # Expected: 0

# Test case 3 (multiple squares)
obj3 = DetectSquares()
obj3.add([5, 10])
obj3.add([10, 5])
obj3.add([10, 10])
obj3.add([5, 5])
obj3.add([3, 0])
obj3.add([8, 0])
obj3.add([8, 5])
obj3.add([3, 5])
res3 = obj3.count([10, 10])
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (duplicate points create multiple squares)
obj4 = DetectSquares()
obj4.add([0, 0])
obj4.add([0, 1])
obj4.add([1, 0])
obj4.add([1, 1])
obj4.add([1, 1])  # duplicate
res4 = obj4.count([1, 1])
print(f"Test case 4: {res4}")  # Expected: 2
