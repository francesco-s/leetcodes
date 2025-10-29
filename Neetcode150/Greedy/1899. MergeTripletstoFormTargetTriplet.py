class Solution:

    def mergeTriplets(self, triplets, target):
        """
        Time Complexity: O(n) where n = len(triplets) — we scan each triplet once.
        Space Complexity: O(1) — only a fixed-size (3) array is used.
        """
        final_max = [0, 0, 0]

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                final_max[0] = max(t[0], final_max[0])
                final_max[1] = max(t[1], final_max[1])
                final_max[2] = max(t[2], final_max[2])
        return final_max == target
# Test cases
solution = Solution()

# Test case 1 (example)
triplets1 = [[2,5,3],[1,8,4],[1,7,5]]
target1 = [2,7,5]
res1 = solution.mergeTriplets(triplets1, target1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example - impossible)
triplets2 = [[3,4,5],[4,5,6]]
target2 = [3,2,5]
res2 = solution.mergeTriplets(triplets2, target2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (example - multiple merges)
triplets3 = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target3 = [5,5,5]
res3 = solution.mergeTriplets(triplets3, target3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (exact match exists)
triplets4 = [[1,2,3],[4,5,6]]
target4 = [1,2,3]
res4 = solution.mergeTriplets(triplets4, target4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (all triplets exceed target)
triplets5 = [[5,5,5],[6,6,6]]
target5 = [4,4,4]
res5 = solution.mergeTriplets(triplets5, target5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (need all triplets)
triplets6 = [[1,1,1],[2,2,2],[3,3,3]]
target6 = [3,3,3]
res6 = solution.mergeTriplets(triplets6, target6)
print(f"Test case 6: {res6}")  # Expected: True
