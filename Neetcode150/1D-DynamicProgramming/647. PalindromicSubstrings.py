class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings in s.

        Time Complexity: O(n^2) - nested loops for all substrings, each dp call is O(1) with memoization
        Space Complexity: O(n^2) - memo dictionary stores results for all (i, j) pairs
        """
        n = len(s)
        res = 0
        memo = {}

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

        for i in range(n):
            for j in range(i, n):
                if dp(i, j):
                    res += 1

        return res


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "abc"
res1 = solution.countSubstrings(s1)
print(f"Test case 1: {res1}")  # Expected: 3 ("a", "b", "c")

# Test case 2 (example)
s2 = "aaa"
res2 = solution.countSubstrings(s2)
print(f"Test case 2: {res2}")  # Expected: 6 ("a", "a", "a", "aa", "aa", "aaa")

# Test case 3 (single char)
s3 = "a"
res3 = solution.countSubstrings(s3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (all different)
s4 = "abcd"
res4 = solution.countSubstrings(s4)
print(f"Test case 4: {res4}")  # Expected: 4

# Test case 5 (palindrome with inner palindromes)
s5 = "aba"
res5 = solution.countSubstrings(s5)
print(f"Test case 5: {res5}")  # Expected: 4 ("a", "b", "a", "aba")

# Test case 6 (long palindrome)
s6 = "racecar"
res6 = solution.countSubstrings(s6)
print(f"Test case 6: {res6}")  # Expected: 10

# Test case 7 (even length palindrome)
s7 = "abba"
res7 = solution.countSubstrings(s7)
print(f"Test case 7: {res7}")  # Expected: 6 ("a", "b", "b", "a", "bb", "abba")

# Test case 8 (no long palindrome)
s8 = "xyz"
res8 = solution.countSubstrings(s8)
print(f"Test case 8: {res8}")  # Expected: 3
