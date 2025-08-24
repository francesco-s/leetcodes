from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity: O(n), where n is the number of temperatures.
        # Each temperature is pushed and popped from the stack at most once.
        # Space Complexity: O(n), for the stack and result array.
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                day, _ = stack.pop()
                result[day] = index - day
            stack.append((index, temperature))

        return result


# Test cases
solution = Solution()

# Test case 1
temperatures1 = [73,74,75,71,69,72,76,73]
result1 = solution.dailyTemperatures(temperatures1)
print(f"Test case 1: {result1}")  # Expected: [1,1,4,2,1,1,0,0]

# Test case 2
temperatures2 = [30,40,50,60]
result2 = solution.dailyTemperatures(temperatures2)
print(f"Test case 2: {result2}")  # Expected: [1,1,1,0]

# Test case 3
temperatures3 = [30,60,90]
result3 = solution.dailyTemperatures(temperatures3)
print(f"Test case 3: {result3}")  # Expected: [1,1,0]

# Test case 4
temperatures4 = [89,62,70,58,47,47,46,76,100,70]
result4 = solution.dailyTemperatures(temperatures4)
print(f"Test case 4: {result4}")  # Expected: [8,1,5,4,3,2,1,1,0,0]

# Test case 5
temperatures5 = [55,38,53,81,61,93,97,32,43,78]
result5 = solution.dailyTemperatures(temperatures5)
print(f"Test case 5: {result5}")  # Expected: [3,1,1,2,1,1,0,2,1,0]

# Test case 6
temperatures6 = [100,90,80,70]
result6 = solution.dailyTemperatures(temperatures6)
print(f"Test case 6: {result6}")  # Expected: [0,0,0,0]
