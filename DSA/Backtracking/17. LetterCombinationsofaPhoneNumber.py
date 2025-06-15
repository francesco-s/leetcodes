class Solution:
    def letterCombinations(self, digits):
        mapping = {'2':'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}

        if not digits:
            return []

        res = []

        def backtrack(i: int, path: list):
            if len(digits) == len(path):
                res.append("".join(path)) 
                return

            possible_letters = mapping[digits[i]]

            for letter in possible_letters:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()

        combinations = []
        backtrack(0, combinations)
        
        return res


# Test cases
solution = Solution()

# Test case 1
digits1 = "23"
print("Test case 1:", solution.letterCombinations(digits1))
# Expected: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# Test case 2
digits2 = ""
print("Test case 2:", solution.letterCombinations(digits2))
# Expected: []

# Test case 3
digits3 = "7"
print("Test case 3:", solution.letterCombinations(digits3))
# Expected: ["p", "q", "r", "s"]