class Solution:
    def makeGood(s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            if len(stack) > 0 and stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)


print(Solution.makeGood(s="leEeetcode"))
print(Solution.makeGood(s="abBAcC"))
