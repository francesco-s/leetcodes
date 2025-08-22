class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append('(')
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(')')
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()

        backtracking([], 0, 0)

        return answer

# Test cases
solution = Solution()

# Test case 1
n1 = 3
result1 = solution.generateParenthesis(n1)
print(f"Test case 1: {result1}")  # Expected: ["((()))","(()())","(())()","()(())","()()()"]

# Test case 2
n2 = 1
result2 = solution.generateParenthesis(n2)
print(f"Test case 2: {result2}")  # Expected: ["()"]

# Test case 3
n3 = 2
result3 = solution.generateParenthesis(n3)
print(f"Test case 3: {result3}")  # Expected: ["(())","()()"]

# Test case 4
n4 = 4
result4 = solution.generateParenthesis(n4)
print(f"Test case 4: {result4}")  # Expected: ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

# Test case 5
n5 = 0
result5 = solution.generateParenthesis(n5)
print(f"Test case 5: {result5}")  # Expected: [""]
