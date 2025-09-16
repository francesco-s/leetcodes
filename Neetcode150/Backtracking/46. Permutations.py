from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of nums.

        TC: O(n * n!), where n is the length of nums, since there are n! permutations and each is built in O(n) time.
        SC: O(n!) for storing the resulting list of permutations, plus O(n) auxiliary space for recursion stack.
        """
        nums_len = len(nums)
        res = []
        used = [False] * nums_len

        def dfs(sub_nums):
            if len(sub_nums) == nums_len:
                res.append(sub_nums[:])
                return

            for i in range(nums_len):
                if not used[i]:
                    used[i] = True
                    sub_nums.append(nums[i])
                    dfs(sub_nums)
                    sub_nums.pop()
                    used[i] = False

        dfs([])
        return res

# Test cases
solution = Solution()

# Test case 1 (example-sized input)
nums1 = [1,2,3]
res1 = solution.permute(nums1)
print(f"Test case 1: {res1}")  # Expected (any order): 6 perms like [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Test case 2 (single element)
nums2 = []
res2 = solution.permute(nums2)
print(f"Test case 2: {res2}")  # Expected: []

# Test case 3 (two elements)
nums3 = [1,2]
res3 = solution.permute(nums3)
print(f"Test case 3: {res3}")  # Expected (any order): [[1,2],[2,1]]

# Test case 4 (four elements -> 24 permutations)
nums4 = [1,2,3,4]
res4 = solution.permute(nums4)
print(f"Test case 4 size: {len(res4)}")  # Expected size: 24

# Test case 5 (includes negative numbers)
nums5 = [-1, 0, 1]
res5 = solution.permute(nums5)
print(f"Test case 5 size: {len(res5)}")  # Expected size: 6

# Test case 6 (empty input edge)
nums6 = []
res6 = solution.permute(nums6)
print(f"Test case 6: {res6}")  # Expected: [[]] by convention
