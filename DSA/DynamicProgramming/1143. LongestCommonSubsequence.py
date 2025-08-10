from functools import lru_cache


class Solution:
    def longestCommonSubsequenceBad(self, text1: str, text2: str) -> int:
    
        @lru_cache(maxsize=None)
        def dp(i, j): 
            # Time Complexity:
            # Each (i, j) pair is memoized, so at most len(text1) * len(text2) calls.
            # However, text2.find() is O(m) for each call, so overall worst-case is O(n * m^2),
            # where n = len(text1), m = len(text2).

            # Space Complexity:
            # The lru_cache stores up to len(text1) * len(text2) entries, so O(n * m) space.
            # The recursion stack depth is at most O(n).

            if len(text1) == i or len(text2) == j:
                return 0

            option_1 = dp(i + 1, j)

            first_occurence = text2.find(text1[i], j) # O(m) per call

            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + dp(i + 1, first_occurence + 1)

            return max(option_1, option_2)
        
        return dp(0, 0)
    

    def longestCommonSubsequenceTD(self, text1: str, text2: str) -> int: # O(n * m) and O(n * m)

        @lru_cache(maxsize=None)
        def dp(i, j):

            if len(text1) == i or len(text2) == j:
                return 0


            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))
        
        return dp(0, 0)
    

    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # O(n * m) and O(n * m)
        n = len(text1)
        m = len(text2)
        dp_grid = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp_grid[i][j] = 1 + dp_grid[i + 1][j + 1]
                else:
                    dp_grid[i][j] = max(dp_grid[i + 1][j], dp_grid[i][j + 1])

        return dp_grid[0][0]
                



# Test cases
solution = Solution()

# Test case 1
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(f"Test case 1: {result}")  # Expected: 3

# Test case 2
text1 = "abc"
text2 = "abc"
result = solution.longestCommonSubsequence(text1, text2)
print(f"Test case 2: {result}")  # Expected: 3

# Test case 3
text1 = "abc"
text2 = "def"
result = solution.longestCommonSubsequence(text1, text2)
print(f"Test case 3: {result}")  # Expected: 0

# Test case 4
text1 = "aggtab"
text2 = "gxtxayb"
result = solution.longestCommonSubsequence(text1, text2)
print(f"Test case 4: {result}")  # Expected: 4