from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = defaultdict(int)

        for char in s:
            char_counter[char] += 1

        for index, char in enumerate(s):
            if char_counter[char] == 1:
                return index
            
        return -1




    def firstUniqCharBrute(self, s: str) -> int:
        # Placeholder for the solution
        if len(s) == 1:
            return 0
        
        for i in range(0, len(s)):
            for j in range(0, len(s)):

                if s[i] == s[j] and j != i:
                    break
                if j == len(s) - 1:
                    return i

                
        return -1




# Test cases
solution = Solution()

# Test case 1
s4 = "dddccdbba"
result4 = solution.firstUniqChar(s4)
print(f"Test case 4: {result4}")  # Expected: 8

# Test case 2
s3 = "z"
result3 = solution.firstUniqChar(s3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 3
s1 = "leetcode"
result1 = solution.firstUniqChar(s1)
print(f"Test case 1: {result1}")  # Expected: 0

# Test case 4
s2 = "loveleetcode"
result2 = solution.firstUniqChar(s2)
print(f"Test case 2: {result2}")  # Expected: 2

# Test case 5
s3 = "aabb"
result3 = solution.firstUniqChar(s3)
print(f"Test case 3: {result3}")  # Expected: -1