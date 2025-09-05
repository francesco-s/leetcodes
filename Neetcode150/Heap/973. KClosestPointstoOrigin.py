from heapq import heappop, heappush
from typing import List


class Solution:

    def kClosestHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Heap-based approach.
        Time Complexity: O(n log n) due to pushing all n points into the heap and popping k times.
        Space Complexity: O(n) for the heap.
        """
        distances = []
        for i, point in enumerate(points):
            squared_distance = point[0]**2 + point[1]**2
            heappush(distances, (squared_distance, i))
        return [points[heappop(distances)[1]] for _ in range(k)]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Sort-based approach.
        Time Complexity: O(n log n) due to sorting all n points.
        Space Complexity: O(1) if sorting in place, otherwise O(n).
        """
        def squared_distance(point):
            return point[0]**2 + point[1]**2
        points.sort(key=squared_distance)
        return points[:k]
    


# Test cases
solution = Solution()

# Test case 1 (example)
points1 = [[1,3],[-2,2]]
k1 = 1
res1 = solution.kClosest(points1, k1)
print(f"Test case 1: {res1}")  # Expected: [[-2,2]]

# Test case 2 (example with more points)
points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2
res2 = solution.kClosest(points2, k2)
print(f"Test case 2: {res2}")  # Expected: [[3,3],[-2,4]]

# Test case 3 (k equals n)
points3 = [[1,1],[2,2],[3,3]]
k3 = 3
res3 = solution.kClosest(points3, k3)
print(f"Test case 3: {res3}")  # Expected: [[1,1],[2,2],[3,3]]

# Test case 4 (ties allowed in any order)
points4 = [[1,0],[0,1],[-1,0],[0,-1]]
k4 = 2
res4 = solution.kClosest(points4, k4)
print(f"Test case 4: {res4}")  # Expected: any two among unit-distance points

# Test case 5 (negative coordinates)
points5 = [[-5,-4],[2,-1],[-2,2],[0,0]]
k5 = 2
res5 = solution.kClosest(points5, k5)
print(f"Test case 5: {res5}")  # Expected: [[0,0],[2,-1]] or [[0,0],[-2,2]]

# Test case 6 (large values)
points6 = [[10000,10000],[-10000,0],[0,-10000],[1,1]]
k6 = 3
res6 = solution.kClosest(points6, k6)
print(f"Test case 6: {res6}")  # Expected: three closest, e.g., [[1,1],[-10000,0],[0,-10000]]
