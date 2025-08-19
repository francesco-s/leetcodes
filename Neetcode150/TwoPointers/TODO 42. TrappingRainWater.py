class Solution:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pass

# Test cases
solution = Solution()

# Test case 1
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
result1 = solution.trap(height1)
print(f"Test case 1: {result1}")  # Expected: 6

# Test case 2
height2 = [4,2,0,3,2,5]
result2 = solution.trap(height2)
print(f"Test case 2: {result2}")  # Expected: 9

# Test case 3
height3 = [0,0,0,0]
result3 = solution.trap(height3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
height4 = [2,0,2]
result4 = solution.trap(height4)
print(f"Test case 4: {result4}")  # Expected: 2

# Test case 5
height5 = [3, 0, 1, 3, 0, 5]
result5 = solution.trap(height5)
print(f"Test case 5: {result5}")  # Expected: 8

# Test case 6
height6 = [1,2,1,3,0,1,2]
result6 = solution.trap(height6)
print(f"Test case 6: {result6}")  # Expected: 3
