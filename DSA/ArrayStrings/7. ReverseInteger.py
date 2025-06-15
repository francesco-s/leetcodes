import math


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        x_reverted = 0

        while x != 0:
            x_reverted = x_reverted * 10 + x % 10
            x //= 10

        x_reverted *= sign

        if x_reverted < -2**31 or x_reverted > 2**31 - 1:
            return 0
        
        return x_reverted

    def reverse2(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if rev > pow(2, 31) - 1:
            return 0
        elif rev < pow(-2, 31):
            return 0
        elif x > 0:
            return rev
        else:
            return -rev


# Test cases
solution = Solution()

# Test case 1
result1 = solution.reverse(-123)
print(f"Test case 1: {result1}")  # Expected: -321

# Test case 2
result2 = solution.reverse(123)
print(f"Test case 2: {result2}")  # Expected: 321

# Test case 3
result3 = solution.reverse(120)
print(f"Test case 3: {result3}")  # Expected: 21

# Test case 4
result4 = solution.reverse(0)
print(f"Test case 4: {result4}")  # Expected: 0

# Test case 5
result5 = solution.reverse(1534236469)
print(f"Test case 5: {result5}")  # Expected: 0 (overflow)

