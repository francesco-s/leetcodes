from typing import List
import heapq


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def squared_distance(point: List[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        points_dist = [(squared_distance(points[i]), [points[i][0], points[i][1]]) for i in range(len(points))]

        heapq.heapify(points_dist)

        res = []
        while k > 0:
            res.append(heapq.heappop(points_dist)[1])
            k -= 1

        return res

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # Since heap is sorted in increasing order,
    #     # negate the distance to simulate max heap
    #     # and fill the heap with the first k elements of points
    #     heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
    #     heapq.heapify(heap)
    #     for i in range(k, len(points)):
    #         dist = -self.squared_distance(points[i])
    #         if dist > heap[0][0]:
    #             # If this point is closer than the kth farthest,
    #             # discard the farthest point and add this one
    #             heapq.heappushpop(heap, (dist, i))
    #
    #     # Return all points stored in the max heap
    #     return [points[i] for (_, i) in heap]
    #
    # def squared_distance(self, point: List[int]) -> int:
    #     """Calculate and return the squared Euclidean distance."""
    #     return point[0] ** 2 + point[1] ** 2

solution = Solution()

points = [[1, 3], [-2, 2]]
k = 1

result = solution.kClosest(points, k)
print("Test case 1 - Expected: [[-2,2]], Got:", result)

points = [[3, 3], [5, -1], [-2, 4]]
k = 2

result = solution.kClosest(points, k)
print("Test case 1 - Expected: [[3,3],[-2,4]], Got:", result)

points = [[0, 1], [1, 0]]
k = 2

result = solution.kClosest(points, k)
print("Test case 1 - Expected: [[0,1], [1,0]], Got:", result)
