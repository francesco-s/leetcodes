# LeetCode 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        left2right = [1] * n
        right2left = [1] * n
        res = [1] * n
        
        for i in range(n):
            left2right[i] = left2right[i - 1] * nums[i]

        right2left[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right2left[i] = right2left[i + 1] * nums[i]

        for i in range(n):
            if i == 0:
                res[i] = right2left[i + 1]
            elif i == n - 1:
                res[i] = left2right[i - 1]
            else:
                res[i] = left2right[i - 1] * right2left[i + 1]

        return res
        

    def productExceptSelfBruteForce(self, nums):
        n = len(nums)
        output_array = [1] * n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                output_array[i] *= nums[j]

        return output_array




# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4]
print(f"Test case 1: {solution.productExceptSelf(nums1)}")  # Expected: [24, 12, 8, 6]

# Test case 2
nums2 = [-1, 1, 0, -3, 3]
print(f"Test case 2: {solution.productExceptSelf(nums2)}")  # Expected: [0, 0, 9, 0, 0]

# Test case 3
nums3 = [2, 3, 4, 5]
print(f"Test case 3: {solution.productExceptSelf(nums3)}")  # Expected: [60, 40, 30, 24]

# Test case 4
nums4 = [0, 0]
print(f"Test case 4: {solution.productExceptSelf(nums4)}")  # Expected: [0, 0]

# Test case 5
nums5 = [1, 0]
print(f"Test case 5: {solution.productExceptSelf(nums5)}")  # Expected: [0, 1]