from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            At each call, we append a copy of the current path.
            Time Complexity (TC): O(2^n) as each element is either included or not.
            Space Complexity (SC): O(n) for the recursion stack and path.
        """
        output = []
        
        def recursion(start, path):

            output.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                recursion(i + 1, path)
                path.pop()
        
        recursion(0, [])
        return output

        
# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [1,2,3]
res1 = solution.subsets(nums1)
print(f"Test case 1: {res1}")  # Expected: 8 subsets in any order, e.g., [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Test case 2 (single element)
nums2 = [0]
res2 = solution.subsets(nums2)
print(f"Test case 2: {res2}")  # Expected: [[],[0]]

# Test case 3 (two elements)
nums3 = [1,2]
res3 = solution.subsets(nums3)
print(f"Test case 3: {res3}")  # Expected: 4 subsets, e.g., [[],[1],[2],[1,2]]

# Test case 4 (empty input -> by constraints not typical, but handle gracefully)
nums4 = []
res4 = solution.subsets(nums4)
print(f"Test case 4: {res4}")  # Expected: [[]]

# Test case 5 (negative numbers)
nums5 = [-1,2]
res5 = solution.subsets(nums5)
print(f"Test case 5: {res5}")  # Expected: [[],[-1],[2],[-1,2]]

# Test case 6 (distinct values, order doesn't matter)
nums6 = [4,5,6]
res6 = solution.subsets(nums6)
print(f"Test case 6 size: {len(res6)}")  # Expected: 8
