class Solution:

    def reverse(self, x):
        """
        Reverse an integer within 32-bit signed integer range.

        Time Complexity: O(log₁₀|x|) - proportional to the number of digits in x
        Space Complexity: O(1) - uses constant extra space
        """
        MAX_INT = 0x7FFFFFFF
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x:
            digit = x % 10
            x //= 10
            res = res * 10 + digit
            if res > MAX_INT:
                return 0
        
        return res * sign

# Test cases
solution = Solution()

# Test case 1 (example - positive)
x1 = 123
res1 = solution.reverse(x1)
print(f"Test case 1: {res1}")  # Expected: 321

# Test case 2 (example - negative)
x2 = -123
res2 = solution.reverse(x2)
print(f"Test case 2: {res2}")  # Expected: -321

# Test case 3 (trailing zeros)
x3 = 120
res3 = solution.reverse(x3)
print(f"Test case 3: {res3}")  # Expected: 21

# Test case 4 (zero)
x4 = 0
res4 = solution.reverse(x4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (overflow case)
x5 = 1534236469
res5 = solution.reverse(x5)
print(f"Test case 5: {res5}")  # Expected: 0 (would overflow)

# Test case 6 (single digit)
x6 = 7
res6 = solution.reverse(x6)
print(f"Test case 6: {res6}")  # Expected: 7

# Test case 7 (negative overflow)
x7 = -2147483648
res7 = solution.reverse(x7)
print(f"Test case 7: {res7}")  # Expected: 0 (would overflow)
