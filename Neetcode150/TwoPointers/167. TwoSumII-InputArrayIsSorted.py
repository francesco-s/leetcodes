from collections import defaultdict


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right =  0, len(numbers) - 1

        while left < right:
            _sum = numbers[left] + numbers[right]

            if _sum == target:
                return [left + 1, right + 1]
            elif _sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]


    
    def twoSumClassic(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        complements = defaultdict(int)

        for i in range(n):
            complement = target - numbers[i]

            if complement in complements:
                return [complements[complement] + 1, i + 1]
            
            complements[numbers[i]] = i

# Test cases
solution = Solution()

# Test case 1
numbers1 = [2, 7, 11, 15]
target1 = 9
result1 = solution.twoSum(numbers1, target1)
print(f"Test case 1: {result1}")  # Expected: [1, 2]

# Test case 2
numbers2 = [2, 3, 4]
target2 = 6
result2 = solution.twoSum(numbers2, target2)
print(f"Test case 2: {result2}")  # Expected: [1, 3]

# Test case 3
numbers3 = [-1, 0]
target3 = -1
result3 = solution.twoSum(numbers3, target3)
print(f"Test case 3: {result3}")  # Expected: [1, 2]

# Test case 4
numbers4 = [1, 2, 3, 4, 4, 9, 56, 90]
target4 = 8
result4 = solution.twoSum(numbers4, target4)
print(f"Test case 4: {result4}")  # Expected: [4, 5]

# Test case 5
numbers5 = [5, 25, 75]
target5 = 100
result5 = solution.twoSum(numbers5, target5)
print(f"Test case 5: {result5}")  # Expected: [2, 3]
