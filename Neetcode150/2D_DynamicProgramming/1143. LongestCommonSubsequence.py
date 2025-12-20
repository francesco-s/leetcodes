class Solution:
    # TC: O(m * n) - We solve O(m * n) distinct subproblems, each taking O(1) work.
    # SC: O(m * n) - The memo dictionary stores O(m * n) states.
    #                The recursion stack depth is O(m + n) in the worst case.
    def longestCommonSubsequence(self, text1, text2):
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[(i, j)]

        return dfs(0, 0)


# Test cases
solution = Solution()

# Test case 1 (example)
text1_1 = "abcde"
text2_1 = "ace"
res1 = solution.longestCommonSubsequence(text1_1, text2_1)
print(f"Test case 1: {res1}")  # Expected: 3 ("ace")

# Test case 2 (example)
text1_2 = "abc"
text2_2 = "abc"
res2 = solution.longestCommonSubsequence(text1_2, text2_2)
print(f"Test case 2: {res2}")  # Expected: 3 ("abc")

# Test case 3 (example)
text1_3 = "abc"
text2_3 = "def"
res3 = solution.longestCommonSubsequence(text1_3, text2_3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (no common chars)
text1_4 = "abc"
text2_4 = "xyz"
res4 = solution.longestCommonSubsequence(text1_4, text2_4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (partially common)
text1_5 = "bsbininm"
text2_5 = "jmjkbkjkv"
res5 = solution.longestCommonSubsequence(text1_5, text2_5)
print(
    f"Test case 5: {res5}"
)  # Expected: 1 ("b" or "k" or "m" etc., depends on sequence, e.g. "b")

# Test case 6 (one string is empty)
text1_6 = ""
text2_6 = "abc"
res6 = solution.longestCommonSubsequence(text1_6, text2_6)
print(f"Test case 6: {res6}")  # Expected: 0

# Test case 7 (long common sub)
text1_7 = "ezupkr"
text2_7 = "ubmrapg"
res7 = solution.longestCommonSubsequence(text1_7, text2_7)
print(f"Test case 7: {res7}")  # Expected: 2 ("ur" or similar)

# Test case 8 (complex)
text1_8 = "mhunuzqrkzsnidwbun"
text2_8 = "szulspmhwpazoxijwbq"
res8 = solution.longestCommonSubsequence(text1_8, text2_8)
print(f"Test case 8: {res8}")  # Expected: 6 ("huz..." or similar)
