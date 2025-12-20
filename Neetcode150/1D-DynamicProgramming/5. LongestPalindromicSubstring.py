# Time Complexity: O(n^2) due to the nested loops and recursive dp calls
# Space Complexity: O(n^2) for the memoization table


class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        n = len(s)

        def dp(i, j):
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1)
            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        max_len = 0
        start = 0

        for i in range(0, n):
            for j in range(i, n):
                if dp(i, j) and max_len < j - i + 1:
                    start = i
                    max_len = j - i + 1

        return s[start : start + max_len]


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "babad"
res1 = solution.longestPalindrome(s1)
print(f"Test case 1: {res1}")  # Expected: "bab" or "aba"

# Test case 2 (example)
s2 = "cbbd"
res2 = solution.longestPalindrome(s2)
print(f"Test case 2: {res2}")  # Expected: "bb"

# Test case 3 (single char)
s3 = "a"
res3 = solution.longestPalindrome(s3)
print(f"Test case 3: {res3}")  # Expected: "a"

# Test case 4 (all same chars)
s4 = "aaaa"
res4 = solution.longestPalindrome(s4)
print(f"Test case 4: {res4}")  # Expected: "aaaa"

# Test case 5 (palindrome at end)
s5 = "abcda"
res5 = solution.longestPalindrome(s5)
print(
    f"Test case 5: {res5}"
)  # Expected: "a" (single char) or similar, but "abcda" isn't palindrome. Correct example: "abacaba" -> "abacaba"

# Test case 6 (entire string palindrome)
s6 = "racecar"
res6 = solution.longestPalindrome(s6)
print(f"Test case 6: {res6}")  # Expected: "racecar"

# Test case 7 (even length palindrome)
s7 = "abba"
res7 = solution.longestPalindrome(s7)
print(f"Test case 7: {res7}")  # Expected: "abba"

# Test case 8 (no long palindrome)
s8 = "ac"
res8 = solution.longestPalindrome(s8)
print(f"Test case 8: {res8}")  # Expected: "a" or "c"
