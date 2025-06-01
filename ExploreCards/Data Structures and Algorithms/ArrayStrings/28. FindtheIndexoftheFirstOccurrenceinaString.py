class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Placeholder for the solution implementation
        win_len = len(needle)

        if win_len == 0:
            return 0

        for i in range(0, len(haystack) - win_len + 1):
            if haystack[i : i + win_len] == needle:
                return i
            
        return -1


    
    def strStrPython(self, haystack: str, needle: str) -> int:
        # Placeholder for the solution implementation
        return haystack.find(needle)

# Test cases
solution = Solution()

# Test case 1
haystack1 = "sadbutsad"
needle1 = "sad"
result1 = solution.strStr(haystack1, needle1)
print(f"Test case 1: {result1}")  # Expected: 0

# Test case 2
haystack2 = "leetcode"
needle2 = "leeto"
result2 = solution.strStr(haystack2, needle2)
print(f"Test case 2: {result2}")  # Expected: -1

# Test case 3
haystack3 = "hello"
needle3 = "ll"
result3 = solution.strStr(haystack3, needle3)
print(f"Test case 3: {result3}")  # Expected: 2

# Test case 4
haystack4 = "aaaaa"
needle4 = "bba"
result4 = solution.strStr(haystack4, needle4)
print(f"Test case 4: {result4}")  # Expected: -1

# Test case 5
haystack5 = ""
needle5 = ""
result5 = solution.strStr(haystack5, needle5)
print(f"Test case 5: {result5}")  # Expected: 0