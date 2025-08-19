class Solution:

    def lengthOfLongestSubstringVerbose(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        left = 0
        longest_sub = 1

        w_seen = set()
        w_seen.add(s[0])

        for right in range(1, len(s)):
            if s[right] not in w_seen:
                longest_sub = max(longest_sub, right - left + 1)
                w_seen.add(s[right])
            else:
                while left < right and s[left] != s[right]:
                    w_seen.remove(s[left])
                    left += 1
                left += 1
        return longest_sub
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        left = 0
        longest_sub = 0
        w_seen = set()

        for right in range(n):
            while s[right] in w_seen:
                w_seen.remove(s[left])
                left += 1

            w_seen.add(s[right])
            longest_sub = max(longest_sub, right - left + 1)

        return longest_sub


# Test cases
solution = Solution()

# Test case 1
s1 = "abcabcbb"
result1 = solution.lengthOfLongestSubstring(s1)
print(f"Test case 1: {result1}")  # Expected: 3

# Test case 2
s2 = "bbbbb"
result2 = solution.lengthOfLongestSubstring(s2)
print(f"Test case 2: {result2}")  # Expected: 1

# Test case 3
s3 = "pwwkew"
result3 = solution.lengthOfLongestSubstring(s3)
print(f"Test case 3: {result3}")  # Expected: 3

# Test case 4
s4 = ""
result4 = solution.lengthOfLongestSubstring(s4)
print(f"Test case 4: {result4}")  # Expected: 0

# Test case 5
s5 = "au"
result5 = solution.lengthOfLongestSubstring(s5)
print(f"Test case 5: {result5}")  # Expected: 2

# Test case 6
s6 = "dvdf"
result6 = solution.lengthOfLongestSubstring(s6)
print(f"Test case 6: {result6}")  # Expected: 3
