# Input : /home/
# Output : /home
#
# Input : /a/./b/../../c/
# Output : /c
#
# Input : /a/..
# Output : /
#
# Input : /a/../
# Ouput : /
#
# Input : /../../../../../a
# Ouput : /a
#
# Input : /a/./b/./c/./d/
# Ouput : /a/b/c/d
#
# Input : /a/../.././../../.
# Ouput : /
#
# Input : /a//b//c//////d
# Ouput : /a/b/c/d


class Solution:
    def isValid(s: str) -> bool:
        stack = []
        matches = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for char in s:
            if len(stack) > 0:
                if matches[stack[-1]] == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack) == 0


print(Solution.isValid("()"))
print(Solution.isValid("()[]{}"))
print(Solution.isValid("(]"))
