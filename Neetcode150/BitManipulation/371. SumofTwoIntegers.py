class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Add two integers without using + or - operators.
        
        Time Complexity: O(1) - Maximum 32 iterations for 32-bit integers
        Space Complexity: O(1) - Only using constant extra space
        """
        mask = 0xFFFFFFFF # 11111111 11111111 11111111 11111111
        max_int = 0x7FFFFFFF # 01111111 11111111 11111111 11111111

        while b != 0:
            sum_without_carry = a ^ b
            carry = (a & b) << 1

            a = sum_without_carry & mask
            b = carry & mask
        
        return a if a <= max_int else ~(a ^ mask) # the same as a - 2**32

# Test cases
solution = Solution()

# Test case 1 (example)
a1, b1 = 1, 2
res1 = solution.getSum(a1, b1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (example)
a2, b2 = 2, 3
res2 = solution.getSum(a2, b2)
print(f"Test case 2: {res2}")  # Expected: 5

# Test case 3 (positive + negative)
a3, b3 = 1, -1
res3 = solution.getSum(a3, b3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (negative + negative)
a4, b4 = -1, -2
res4 = solution.getSum(a4, b4)
print(f"Test case 4: {res4}")  # Expected: -3

# Test case 5 (with zero)
a5, b5 = 5, 0
res5 = solution.getSum(a5, b5)
print(f"Test case 5: {res5}")  # Expected: 5

# Test case 6 (both zeros)
a6, b6 = 0, 0
res6 = solution.getSum(a6, b6)
print(f"Test case 6: {res6}")  # Expected: 0

# Test case 7 (larger numbers)
a7, b7 = 20, 30
res7 = solution.getSum(a7, b7)
print(f"Test case 7: {res7}")  # Expected: 50

# Test case 8 (negative + positive)
a8, b8 = -2, 3
res8 = solution.getSum(a8, b8)
print(f"Test case 8: {res8}")  # Expected: 1
