class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Time Complexity: O(n) - each index is computed once and memoized
        Space Complexity: O(n) - memo dictionary stores results for each index
        """
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i == len(s) - 1:
                return 1

            ans = dp(i + 1)
            if int(s[i : i + 2]) <= 26:
                ans += dp(i + 2)

            memo[i] = ans

            return ans

        return dp(0)


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "12"
res1 = solution.numDecodings(s1)
print(f"Test case 1: {res1}")  # Expected: 2 ("AB", "L")

# Test case 2 (example)
s2 = "226"
res2 = solution.numDecodings(s2)
print(f"Test case 2: {res2}")  # Expected: 3 ("BZ", "VF", "BBF")

# Test case 3 (example - leading zero)
s3 = "06"
res3 = solution.numDecodings(s3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (single char - valid)
s4 = "1"
res4 = solution.numDecodings(s4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5 (single char - zero)
s5 = "0"
res5 = solution.numDecodings(s5)
print(f"Test case 5: {res5}")  # Expected: 0

# Test case 6 (mid-string zero)
s6 = "10"
res6 = solution.numDecodings(s6)
print(f"Test case 6: {res6}")  # Expected: 1 ("J")

# Test case 7 (invalid mid-string zero)
s7 = "230"
res7 = solution.numDecodings(s7)
print(f"Test case 7: {res7}")  # Expected: 0

# Test case 8 (large number - sequence)
s8 = "11111"
res8 = solution.numDecodings(s8)
print(f"Test case 8: {res8}")  # Expected: 8
