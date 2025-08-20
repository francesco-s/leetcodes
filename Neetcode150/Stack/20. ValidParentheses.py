class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:  # Odd length strings can't be valid
            return False

        map_parenthesis = {
            ")" : "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != map_parenthesis[char]:
                return False
        
        return not stack

# Test cases
solution = Solution()

# Test case 1
s1 = "()"
result1 = solution.isValid(s1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
s2 = "()[]{}"
result2 = solution.isValid(s2)
print(f"Test case 2: {result2}")  # Expected: True

# Test case 3
s3 = "(]"
result3 = solution.isValid(s3)
print(f"Test case 3: {result3}")  # Expected: False

# Test case 4
s4 = "([)]"
result4 = solution.isValid(s4)
print(f"Test case 4: {result4}")  # Expected: False

# Test case 5
s5 = "{[]}"
result5 = solution.isValid(s5)
print(f"Test case 5: {result5}")  # Expected: True

# Test case 6
s6 = ""
result6 = solution.isValid(s6)
print(f"Test case 6: {result6}")  # Expected: True

# Test case 7
s7 = "((("
result7 = solution.isValid(s7)
print(f"Test case 7: {result7}")  # Expected: False

# Test case 8
s8 = ")))"
result8 = solution.isValid(s8)
print(f"Test case 8: {result8}")  # Expected: False
