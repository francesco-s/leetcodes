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
    def simplifyPath(path: str) -> str:
        stack = []
        for sub in path.split("/"):
            if stack and sub == '..':
                stack.pop()
            elif sub == '.' or sub == '':
                continue
            elif sub != '..':
                stack.append(sub)

        return "/" + "/".join(stack)


print(Solution.simplifyPath("/home/"))
print(Solution.simplifyPath("/home//foo/"))
print(Solution.simplifyPath("/home/user/Documents/../Pictures"))
print(Solution.simplifyPath("/.../a/../b/c/../d/./"))
print(Solution.simplifyPath("/../"))
