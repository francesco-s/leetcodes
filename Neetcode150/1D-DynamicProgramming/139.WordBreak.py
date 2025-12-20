from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time Complexity: O(n^2 * m)
        # - n^2: checking all substrings s[i:j]
        # - m: average length of words in dictionary (for "in" check on set)
        # Space Complexity: O(n + k)
        # - n: memoization dictionary stores results for each position (0 to n)
        # - k: word_set stores all unique words from wordDict

        memo = {}
        n = len(s)
        word_set = set(wordDict)

        def dp(i):
            if i in memo:
                return memo[i]
            if i == n:
                return True

            for j in range(i, n + 1):
                if s[i:j] in word_set:
                    if dp(j):
                        memo[i] = True
                        return True

            memo[i] = False
            return memo[i]

        return dp(0)


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "leetcode"
wordDict1 = ["leet", "code"]
res1 = solution.wordBreak(s1, wordDict1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example)
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
res2 = solution.wordBreak(s2, wordDict2)
print(f"Test case 2: {res2}")  # Expected: True

# Test case 3 (example - no segmentation)
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
res3 = solution.wordBreak(s3, wordDict3)
print(f"Test case 3: {res3}")  # Expected: False

# Test case 4 (empty string)
s4 = ""
wordDict4 = ["a"]
res4 = solution.wordBreak(s4, wordDict4)
print(f"Test case 4: {res4}")  # Expected: True (base case i==n)

# Test case 5 (single character)
s5 = "a"
wordDict5 = ["b"]
res5 = solution.wordBreak(s5, wordDict5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (overlapping words)
s6 = "cars"
wordDict6 = ["car", "ca", "rs"]
res6 = solution.wordBreak(s6, wordDict6)
print(f"Test case 6: {res6}")  # Expected: True
