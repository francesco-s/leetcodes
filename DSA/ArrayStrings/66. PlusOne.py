# LeetCode Problem 66: Plus One
# Problem description: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            i = 1
            digits[-i] = 0
            while i < len(digits):
                i += 1
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] += 1
                    return digits
            return [1] + digits
            

# Test cases
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Expected: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # Expected: [4, 3, 2, 2]
print(solution.plusOne([0]))  # Expected: [1]
print(solution.plusOne([9]))  # Expected: [1, 0]
print(solution.plusOne([9, 9, 9]))  # Expected: [1, 0, 0, 0]
print(solution.plusOne([8, 9, 9, 9]))  # Expected: [9, 0, 0, 0]