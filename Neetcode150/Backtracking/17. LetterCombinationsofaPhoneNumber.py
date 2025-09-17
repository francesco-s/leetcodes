from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations that the number could represent.
        
        TC: O(4^n * n) - In the worst case (n digits with 4 letters each), 
            we generate 4^n combinations and concatenating each combination costs O(n).
        SC: O(4^n * n) - The space for storing the combinations, plus O(n) recursion stack space.
        """
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, comb):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            for char in digit_to_char[digits[i]]:
                comb.append(char)
                dfs(i + 1, comb)
                comb.pop()
        
        if digits:
            dfs(0, [])

        return res

# Test cases
solution = Solution()

# Test case 1 (example)
digits1 = "23"
res1 = solution.letterCombinations(digits1)
print(f"Test case 1: {res1}")  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"] in any order

# Test case 2 (empty -> empty list)
digits2 = ""
res2 = solution.letterCombinations(digits2)
print(f"Test case 2: {res2}")  # Expected: []

# Test case 3 (single digit)
digits3 = "2"
res3 = solution.letterCombinations(digits3)
print(f"Test case 3: {res3}")  # Expected: ["a","b","c"] in any order

# Test case 4 (includes a digit mapping to 4 letters)
digits4 = "79"
res4 = solution.letterCombinations(digits4)
print(f"Test case 4 size: {len(res4)}")  # Expected size: 4 * 4 = 16

# Test case 5 (three digits, mix of 3- and 4-letter keys)
digits5 = "274"
res5 = solution.letterCombinations(digits5)
print(f"Test case 5 size: {len(res5)}")  # Expected size: 3 * 4 * 3 = 36

# Test case 6 (repeated digits)
digits6 = "22"
res6 = solution.letterCombinations(digits6)
print(f"Test case 6 size: {len(res6)}")  # Expected size: 3 * 3 = 9
