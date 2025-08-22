class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    stack.append(op2 + op1)
                elif token == '-':
                    print(op2, op1)
                    stack.append(op2 - op1)
                elif token == '*':
                    stack.append(op2 * op1)
                else:
                    stack.append(int(op2 / op1))
        
        return stack.pop()
    
# Test cases
solution = Solution()

# Test case 1
tokens1 = ["2","1","+","3","*"]
result1 = solution.evalRPN(tokens1)
print(f"Test case 1: {result1}")  # Expected: 9

# Test case 2
tokens2 = ["4","13","5","/","+"]
result2 = solution.evalRPN(tokens2)
print(f"Test case 2: {result2}")  # Expected: 6

# Test case 3
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result3 = solution.evalRPN(tokens3)
print(f"Test case 3: {result3}")  # Expected: 22

# Test case 4
tokens4 = ["3","11","+","5","-"]
result4 = solution.evalRPN(tokens4)
print(f"Test case 4: {result4}")  # Expected: 9

# Test case 5
tokens5 = ["18"]
result5 = solution.evalRPN(tokens5)
print(f"Test case 5: {result5}")  # Expected: 18

# Test case 6
tokens6 = ["4","3","-"]
result6 = solution.evalRPN(tokens6)
print(f"Test case 6: {result6}")  # Expected: 1

# Test case 7
tokens7 = ["15","7","1","1","+","/","/","3","*","2","1","1","+","+","-"]
result7 = solution.evalRPN(tokens7)
print(f"Test case 7: {result7}")  # Expected: 5
