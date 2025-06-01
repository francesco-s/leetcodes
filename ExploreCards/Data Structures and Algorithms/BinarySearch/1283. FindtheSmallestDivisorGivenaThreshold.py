from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold):
        left = 1
        right = max(nums)
        ans = 0

        while left <= right:
            middle = (left + right) // 2

            result = 0
            for num in nums:
                result += ceil((1.0 * num) / middle)
            
            if result <= threshold:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return ans


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 5, 9]
threshold1 = 6
result1 = solution.smallestDivisor(nums1, threshold1)
print(f"Test case 1: {result1}")  # Expected: 5

# Test case 2
nums2 = [2, 3, 5, 7, 11]
threshold2 = 11
result2 = solution.smallestDivisor(nums2, threshold2)
print(f"Test case 2: {result2}")  # Expected: (add expected output)