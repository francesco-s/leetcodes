from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Time Complexity: O(n) - single pass over stations
        Space Complexity: O(1) - constant extra space
        """
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res

# Test cases
solution = Solution()

# Test case 1 (example)
gas1 = [1,2,3,4,5]
cost1 = [3,4,5,1,2]
res1 = solution.canCompleteCircuit(gas1, cost1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (impossible)
gas2 = [2,3,4]
cost2 = [3,4,3]
res2 = solution.canCompleteCircuit(gas2, cost2)
print(f"Test case 2: {res2}")  # Expected: -1

# Test case 3 (start at beginning)
gas3 = [5,1,2,3,4]
cost3 = [4,4,1,5,1]
res3 = solution.canCompleteCircuit(gas3, cost3)
print(f"Test case 3: {res3}")  # Expected: 4

# Test case 4 (single station)
gas4 = [1]
cost4 = [2]
res4 = solution.canCompleteCircuit(gas4, cost4)
print(f"Test case 4: {res4}")  # Expected: -1

# Test case 5 (single station possible)
gas5 = [2]
cost5 = [1]
res5 = solution.canCompleteCircuit(gas5, cost5)
print(f"Test case 5: {res5}")  # Expected: 0

# Test case 6 (exact match)
gas6 = [3,3,4]
cost6 = [3,4,4]
res6 = solution.canCompleteCircuit(gas6, cost6)
print(f"Test case 6: {res6}")  # Expected: 2 (or valid start)
