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
    

##########################################################
# Rush 2


class Solution1:
    def isValid(s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0:
                if c in ('(', '[', '{'):
                    stack.append(c)
                else:
                    popped = stack.pop()
                    if popped == '(' and c == ')':
                        continue
                    elif popped == '[' and c == ']':
                        continue
                    elif popped == '{' and c == '}':
                        continue
                    return False
            else:
                stack.append(c)
        
        return True


print(Solution1.isValid("()"))
print(Solution1.isValid("()[]{}"))
print(Solution1.isValid("(]"))
