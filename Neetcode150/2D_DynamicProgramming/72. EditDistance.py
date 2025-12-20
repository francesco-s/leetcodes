from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time Complexity: O(m * n) where m and n are the lengths of the two words. Each pair of indices (i,j) is computed only once due to @cache
        Space Complexity: O(m * n) for memoization (plus O(m + n) recursion stack) => O(m * n)
        """
        m, n = len(word1), len(word2)

        @cache
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

        return dfs(0, 0)


# Test cases
solution = Solution()

# Test case 1 (example)
word1_1 = "horse"
word2_1 = "ros"
res1 = solution.minDistance(word1_1, word2_1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (example)
word1_2 = "intention"
word2_2 = "execution"
res2 = solution.minDistance(word1_2, word2_2)
print(f"Test case 2: {res2}")  # Expected: 5

# Test case 3 (one empty string)
word1_3 = ""
word2_3 = "a"
res3 = solution.minDistance(word1_3, word2_3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (both empty)
word1_4 = ""
word2_4 = ""
res4 = solution.minDistance(word1_4, word2_4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (same strings)
word1_5 = "abc"
word2_5 = "abc"
res5 = solution.minDistance(word1_5, word2_5)
print(f"Test case 5: {res5}")  # Expected: 0

# Test case 6 (replace only)
word1_6 = "abc"
word2_6 = "def"
res6 = solution.minDistance(word1_6, word2_6)
print(f"Test case 6: {res6}")  # Expected: 3

# Test case 7 (insert only)
word1_7 = "abc"
word2_7 = "abcde"
res7 = solution.minDistance(word1_7, word2_7)
print(f"Test case 7: {res7}")  # Expected: 2

# Test case 8 (delete only)
word1_8 = "abcde"
word2_8 = "abc"
res8 = solution.minDistance(word1_8, word2_8)
print(f"Test case 8: {res8}")  # Expected: 2
