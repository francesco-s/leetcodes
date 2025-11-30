class Solution:
    def climbStairs(self, n):
        """
        Time Complexity (TC): O(n)
        Space Complexity (SC): O(n) due to recursion stack and cache
        """
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                if i == n:
                    return 1
                else:
                    return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 2
res1 = solution.climbStairs(n1)
print(f"Test case 1: {res1}")  # Expected: 2

# Test case 2 (example)
n2 = 3
res2 = solution.climbStairs(n2)
print(f"Test case 2: {res2}")  # Expected: 3

# Test case 3 (single step)
n3 = 1
res3 = solution.climbStairs(n3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (four steps)
n4 = 4
res4 = solution.climbStairs(n4)
print(f"Test case 4: {res4}")  # Expected: 5

# Test case 5 (five steps)
n5 = 5
res5 = solution.climbStairs(n5)
print(f"Test case 5: {res5}")  # Expected: 8

# Test case 6 (larger number)
n6 = 10
res6 = solution.climbStairs(n6)
print(f"Test case 6: {res6}")  # Expected: 89

# Test case 7 (edge case)
n7 = 0
res7 = solution.climbStairs(n7)
print(f"Test case 7: {res7}")  # Expected: 1 (staying at ground)
