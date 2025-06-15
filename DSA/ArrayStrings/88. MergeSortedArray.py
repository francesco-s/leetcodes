class Solution:
    def merge(self, nums1, m, nums2, n):
        # Placeholder for the solution

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = m - 1
        p2 = n - 1

        for i in range(-1, -(n + m + 1) , -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1




                

# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
print(f"Test case 1: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]

# Test case 2
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
solution.merge(nums1, m, nums2, n)
print(f"Test case 2: {nums1}")  # Expected: [1, 2, 3, 4, 5, 6]

# Test case 3
nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)
print(f"Test case 3: {nums1}")  # Expected: [1]

# Test case 4
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
print(f"Test case 4: {nums1}")  # Expected: [1]