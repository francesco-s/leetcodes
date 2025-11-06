class Solution:

    def myPow(self, x: float, n: int) -> float:
        """
        Time Complexity: O(|n|) — we perform |n| multiplications in the loop.
        Space Complexity: O(1) — only constant extra space is used.
        """
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        for i in range(abs(n)):
            res *= x

        return res if n >= 0 else 1/res
    
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return res if n % 2 == 0 else res * x

        pow = helper(x, abs(n))
        return pow if n >= 0 else 1 / pow

# Test cases
solution = Solution()

# Test case 1 (example - positive exponent)
x1, n1 = 2.00000, 10
res1 = solution.myPow(x1, n1)
print(f"Test case 1: {res1}")  # Expected: 1024.00000

# Test case 2 (example - small exponent)
x2, n2 = 2.10000, 3
res2 = solution.myPow(x2, n2)
print(f"Test case 2: {res2}")  # Expected: 9.26100

# Test case 3 (example - negative exponent)
x3, n3 = 2.00000, -2
res3 = solution.myPow(x3, n3)
print(f"Test case 3: {res3}")  # Expected: 0.25000

# Test case 4 (zero exponent)
x4, n4 = 3.00000, 0
res4 = solution.myPow(x4, n4)
print(f"Test case 4: {res4}")  # Expected: 1.00000

# Test case 5 (exponent of 1)
x5, n5 = 5.00000, 1
res5 = solution.myPow(x5, n5)
print(f"Test case 5: {res5}")  # Expected: 5.00000

# Test case 6 (negative base with even exponent)
x6, n6 = -2.00000, 2
res6 = solution.myPow(x6, n6)
print(f"Test case 6: {res6}")  # Expected: 4.00000

# Test case 7 (negative base with odd exponent)
x7, n7 = -2.00000, 3
res7 = solution.myPow(x7, n7)
print(f"Test case 7: {res7}")  # Expected: -8.00000

# Test case 8 (large negative exponent)
x8, n8 = 2.00000, -10
res8 = solution.myPow(x8, n8)
print(f"Test case 8: {res8}")  # Expected: 0.0009765625
