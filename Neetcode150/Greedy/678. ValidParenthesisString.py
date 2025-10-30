class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Check if string is valid with '*' as '(', ')' or empty.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        par = []
        ast = []

        for i, c in enumerate(s):
            if c == '(':
                par.append(i)
            elif c == '*':
                ast.append(i)
            else:
                if par:
                    par.pop()
                elif ast:
                    ast.pop()
                else:
                    return False

        while par and ast:
            if par.pop() > ast.pop():
                return False

        return not par
    
    def checkValidStringGreedy(self, s: str) -> bool:
        """
        Greedy check using low/high possible count of open parentheses.
        low  = minimum possible number of unmatched '(' after processing the prefix
               (treat '*' as ')' when minimizing).
        high = maximum possible number of unmatched '(' after processing the prefix
               (treat '*' as '(' when maximizing).
        If high becomes negative there are too many ')' and the string is invalid.
        At the end, low must be 0 for the string to be valid.
        Time: O(n), Space: O(1)
        """
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low = max(low - 1, 0)
                high -= 1
            else:  # c == '*'
                low = max(low - 1, 0)  # treat '*' as ')'
                high += 1             # treat '*' as '('
            if high < 0:
                return False
        return low == 0

# Test cases
solution = Solution()

# Test case 1 (example - simple)
s1 = "()"
res1 = solution.checkValidString(s1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example - wildcard as empty)
s2 = "(*)"
res2 = solution.checkValidString(s2)
print(f"Test case 2: {res2}")  # Expected: True

# Test case 3 (example - wildcard as left paren)
s3 = "(*))"
res3 = solution.checkValidString(s3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (invalid - right before left)
s4 = ")(*"
res4 = solution.checkValidString(s4)
print(f"Test case 4: {res4}")  # Expected: False

# Test case 5 (multiple wildcards)
s5 = "(*)(*)"
res5 = solution.checkValidString(s5)
print(f"Test case 5: {res5}")  # Expected: True

# Test case 6 (all wildcards)
s6 = "***"
res6 = solution.checkValidString(s6)
print(f"Test case 6: {res6}")  # Expected: True

# Test case 7 (complex case)
s7 = "(((******))"
res7 = solution.checkValidString(s7)
print(f"Test case 7: {res7}")  # Expected: True

# Test case 8 (invalid - too many right)
s8 = "((()))()()"
res8 = solution.checkValidString(s8)
print(f"Test case 8: {res8}")  # Expected: True
