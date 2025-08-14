# LeetCode 242: Valid Anagram
# https://leetcode.com/problems/valid-anagram/
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_t[ord(char) - ord('a')] += 1

        return count_t == count_s

    def isAnagramBuildIn(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Test cases
solution = Solution()

# Test case 1
s1, t1 = "anagram", "nagaram"
print(f"Test case 1: {solution.isAnagram(s1, t1)}")  # Expected: True

# Test case 2
s2, t2 = "rat", "car"
print(f"Test case 2: {solution.isAnagram(s2, t2)}")  # Expected: False

# Test case 3
s3, t3 = "", ""
print(f"Test case 3: {solution.isAnagram(s3, t3)}")  # Expected: True

# Test case 4
s4, t4 = "aacc", "ccac"
print(f"Test case 4: {solution.isAnagram(s4, t4)}")  # Expected: False
