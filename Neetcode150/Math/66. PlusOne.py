from typing import List


class Solution:

    def plusOne(self, digits):
        """
        Increment the integer represented by the list `digits` by one.
        TC: O(n)
        SC: O(n)
        """
        if not digits:
            return [1]
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        return self.plusOne(digits[:-1]) + [0] # The [0] acts as the result of 1 + 9 = 1 + [0]
    
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits

# Test cases
solution = Solution()

# Test case 1 (example - simple increment)
digits1 = [1,2,3]
res1 = solution.plusOne(digits1)
print(f"Test case 1: {res1}")  # Expected: [1,2,4]

# Test case 2 (example - carry across)
digits2 = [4,3,2,1]
res2 = solution.plusOne(digits2)
print(f"Test case 2: {res2}")  # Expected: [4,3,2,2]

# Test case 3 (all nines)
digits3 = [9,9,9]
res3 = solution.plusOne(digits3)
print(f"Test case 3: {res3}")  # Expected: [1,0,0,0]

# Test case 4 (single digit)
digits4 = [1]
res4 = solution.plusOne(digits4)
print(f"Test case 4: {res4}")  # Expected: [2]

# Test case 5 (single nine)
digits5 = [9]
res5 = solution.plusOne(digits5)
print(f"Test case 5: {res5}")  # Expected: [1,0]

# Test case 6 (trailing nines)
digits6 = [1,2,9,9]
res6 = solution.plusOne(digits6)
print(f"Test case 6: {res6}")  # Expected: [1,3,0,0]

# Test case 7 (zero)
digits7 = [0]
res7 = solution.plusOne(digits7)
print(f"Test case 7: {res7}")  # Expected: [1]

# Test case 8 (mixed with nines at end)
digits8 = [2,9,9,9]
res8 = solution.plusOne(digits8)
print(f"Test case 8: {res8}")  # Expected: [3,0,0,0]
