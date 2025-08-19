class Solution:
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        absolute_max = 0

        while left < right:
            absolute_max = max(absolute_max, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return absolute_max

# Test cases
solution = Solution()

# Test case 1
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result1 = solution.maxArea(height1)
print(f"Test case 1: {result1}")  # Expected: 49

# Test case 2
height2 = [1, 1]
result2 = solution.maxArea(height2)
print(f"Test case 2: {result2}")  # Expected: 1

# Test case 3
height3 = [1, 2, 1]
result3 = solution.maxArea(height3)
print(f"Test case 3: {result3}")  # Expected: 2

# Test case 4
height4 = [2, 3, 4, 5, 18, 17, 6]
result4 = solution.maxArea(height4)
print(f"Test case 4: {result4}")  # Expected: 17

# Test case 5
height5 = [1, 2, 4, 3]
result5 = solution.maxArea(height5)
print(f"Test case 5: {result5}")  # Expected: 4

# Test case 6
height6 = [1, 8, 100, 2, 100, 4, 8, 3, 7]
result6 = solution.maxArea(height6)
print(f"Test case 6: {result6}")  # Expected: 200
