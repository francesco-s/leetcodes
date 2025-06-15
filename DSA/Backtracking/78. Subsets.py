class Solution:
    def subsets(self, nums):
        res = []

        def backtracking(i, curr):
            if i > len(nums):
                return
            
            res.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtracking(j + 1, curr)
                curr.pop()

        
        backtracking(0, [])
        return res


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3]
result1 = solution.subsets(nums1)
print(f"Test case 1: {result1}")  # Expected: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# Test case 2
nums2 = []
result2 = solution.subsets(nums2)
print(f"Test case 2: {result2}")  # Expected: [[]]