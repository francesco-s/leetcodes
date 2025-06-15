# LeetCode Problem 278: First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    # Mock implementation for testing purposes
    # Replace this with the actual logic or API call
    bad_version = 5  # Example: Assume version 5 is the first bad version
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            middle = left + ((right - left) // 2)
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        
        return left
    
    def firstBadVersionOverflow(self, n: int) -> int:
        # Placeholder for the actual implementation
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Test cases
solution = Solution()

# Test case 1
n1 = 5
# Assuming isBadVersion(4) = False and isBadVersion(5) = True
print(f"Test case 1: {solution.firstBadVersion(n1)}")  # Expected: 5

# Test case 2
n2 = 1
# Assuming isBadVersion(1) = True
print(f"Test case 2: {solution.firstBadVersion(n2)}")  # Expected: 1

# Test case 3
n3 = 10
# Assuming isBadVersion(7) = True and isBadVersion(6) = False
print(f"Test case 3: {solution.firstBadVersion(n3)}")  # Expected: 7