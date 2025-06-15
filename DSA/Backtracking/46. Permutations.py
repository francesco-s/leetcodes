class Solution:
    def permute(self, nums):
        res = []

        def backtracking(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()
        
        backtracking([])
        return res

# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3]
result1 = solution.permute(nums1)
print(f"Test case 1: {result1}")  # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]