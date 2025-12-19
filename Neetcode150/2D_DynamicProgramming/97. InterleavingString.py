from functools import lru_cache


class Solution:
    # TC: O(m * n) where m = len(s1), n = len(s2)
    #     We have at most m * n unique states (i, j combinations)
    # SC: O(m * n) for the memoization cache + O(m + n) for recursion stack
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache
        def dfs(i, j):
            k = i + j

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    return True

            return False


# Test cases
solution = Solution()

# Test case 1 (example)
s1_1 = "aabcc"
s2_1 = "dbbca"
s3_1 = "aadbbcbcac"
res1 = solution.isInterleave(s1_1, s2_1, s3_1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example)
s1_2 = "aabcc"
s2_2 = "dbbca"
s3_2 = "aadbbbaccc"
res2 = solution.isInterleave(s1_2, s2_2, s3_2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (empty strings)
s1_3 = ""
s2_3 = ""
s3_3 = ""
res3 = solution.isInterleave(s1_3, s2_3, s3_3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (length mismatch)
s1_4 = "a"
s2_4 = "b"
s3_4 = "ab"
res4 = solution.isInterleave(s1_4, s2_4, s3_4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (length mismatch - too long)
s1_5 = "a"
s2_5 = "b"
s3_5 = "abc"
res5 = solution.isInterleave(s1_5, s2_5, s3_5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (one empty)
s1_6 = ""
s2_6 = "abc"
s3_6 = "abc"
res6 = solution.isInterleave(s1_6, s2_6, s3_6)
print(f"Test case 6: {res6}")  # Expected: True

# Test case 7 (alternating)
s1_7 = "abc"
s2_7 = "def"
s3_7 = "adbecf"
res7 = solution.isInterleave(s1_7, s2_7, s3_7)
print(f"Test case 7: {res7}")  # Expected: True

# Test case 8 (similar prefix)
s1_8 = "a"
s2_8 = "b"
s3_8 = "a"
res8 = solution.isInterleave(s1_8, s2_8, s3_8)
print(f"Test case 8: {res8}")  # Expected: False (length mismatch)
