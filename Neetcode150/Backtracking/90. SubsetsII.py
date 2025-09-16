from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(2^n * n) in the worst-case, where n is the number of elements.
        # Space Complexity: O(2^n * n) due to the space required for the output and O(n) for the recursion stack.
        res = []
        nums_len = len(nums)
        nums.sort()

        def dfs(i, curr):
            res.append(curr[:])

            for j in range(i, nums_len):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()

        dfs(0, [])
        return res

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [1,2,2]
res1 = solution.subsetsWithDup(nums1)
print(f"Test case 1: {res1}")  # Expected: [[],[1],[1,2],[1,2,2],[2],[2,2]] in any order

# Test case 2 (single)
nums2 = [0]
res2 = solution.subsetsWithDup(nums2)
print(f"Test case 2: {res2}")  # Expected: [[],[0]]

# Test case 3 (all duplicates)
nums3 = [2,2,2]
res3 = solution.subsetsWithDup(nums3)
print(f"Test case 3: {res3}")  # Expected: [[],[2],[2,2],[2,2,2]]

# Test case 4 (negatives and duplicates)
nums4 = [-1,0,0,1]
res4 = solution.subsetsWithDup(nums4)
print(f"Test case 4: {res4}")  # Expected includes [[],[-1],[0],[0,0],[1],[-1,0],[-1,0,0],[-1,1],[0,1],[0,0,1],[-1,0,1],[-1,0,0,1]]

# Test case 5 (mixed with multiple dup groups)
nums5 = [1,1,2,2,3]
res5 = solution.subsetsWithDup(nums5)
print(f"Test case 5 size: {len(res5)}")  # Expected size: 3*3*2 = 18 unique subsets

# Test case 6 (empty input edge)
nums6 = []
res6 = solution.subsetsWithDup(nums6)
print(f"Test case 6: {res6}")  # Expected: [[]]
