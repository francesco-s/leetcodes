class Solution:

    def singleNumber(self, nums):
        """
        Finds the single number in a list where every other number appears twice.

        Args:
            nums (List[int]): List of integers where every element appears twice except for one.

        Returns:
            int: The single number that appears only once.

        Description:
            Uses bitwise XOR to cancel out numbers appearing twice, leaving the unique number.
            Thanks to the characteristic of XOR (a ^ a = 0 and a ^ 0 = a), all duplicates cancel out, leaving the unique number.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1), uses constant extra space.
        """
        result = 0
        for number in nums:
            result = result ^ number
        return result


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [2,2,1]
res1 = solution.singleNumber(nums1)
print(f"Test case 1: {res1}")  # Expected: 1

# Test case 2 (example)
nums2 = [4,1,2,1,2]
res2 = solution.singleNumber(nums2)
print(f"Test case 2: {res2}")  # Expected: 4

# Test case 3 (single element)
nums3 = [1]
res3 = solution.singleNumber(nums3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (negative numbers)
nums4 = [-1,-1,-2]
res4 = solution.singleNumber(nums4)
print(f"Test case 4: {res4}")  # Expected: -2

# Test case 5 (larger array)
nums5 = [7,2,7,9,2]
res5 = solution.singleNumber(nums5)
print(f"Test case 5: {res5}")  # Expected: 9

# Test case 6 (zero included)
nums6 = [0,1,0]
res6 = solution.singleNumber(nums6)
print(f"Test case 6: {res6}")  # Expected: 1

# Test case 7 (multiple duplicates)
nums7 = [3,3,5,5,7,7,9]
res7 = solution.singleNumber(nums7)
print(f"Test case 7: {res7}")  # Expected: 9
