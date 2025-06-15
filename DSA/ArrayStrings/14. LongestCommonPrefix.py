class Solution:
    def longestCommonPrefix(self, strs):
        """
        Placeholder for the solution method.
        """
        if not strs:
            return ""
                
        if len(strs) == 1:
            return strs[0]
        
        longest_common_prefix = 0

        for index, char in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if index < len(strs[i]) and char == strs[i][index]:
                    if i == len(strs) - 1:
                        longest_common_prefix += 1
                else:
                    return strs[0][:longest_common_prefix]

        return strs[0][:longest_common_prefix]

            


# Test cases
solution = Solution()

# Test case 1
strs1 = ["flower", "flow", "flight"]
result1 = solution.longestCommonPrefix(strs1)
print(f"Test case 1: {result1}")  # Expected: "fl"

# Test case 2
strs2 = ["dog", "racecar", "car"]
result2 = solution.longestCommonPrefix(strs2)
print(f"Test case 2: {result2}")  # Expected: ""

# Test case 3
strs3 = ["interspecies", "interstellar", "interstate"]
result3 = solution.longestCommonPrefix(strs3)
print(f"Test case 3: {result3}")  # Expected: "inters"

# Test case 4
strs4 = ["", "b"]
result4 = solution.longestCommonPrefix(strs4)
print(f"Test case 4: {result4}")  # Expected: ""

# Test case 5
strs5 = ["a"]
result5 = solution.longestCommonPrefix(strs5)
print(f"Test case 5: {result5}")  # Expected: "a"

# Test case 6
strs6 = ["cir", "car"]
result6 = solution.longestCommonPrefix(strs6)
print(f"Test case 6: {result6}")  # Expected: "c"