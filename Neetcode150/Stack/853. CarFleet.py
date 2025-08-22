from typing import List


class Solution:
    def carFleetStack(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by position
        cars = sorted(zip(position, speed))
        times = [(target - pos) / sp for pos, sp in cars]

        stack = []
        for t in times[::-1]:
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / sp for pos, sp in cars]

        curr_time = 0
        fleets = 0
        
        for t in times:
            if t > curr_time:
                fleets += 1
                curr_time = t
        
        return fleets

# Test cases
solution = Solution()

# Test case 1
target1 = 12
position1 = [10,8,0,5,3]
speed1 = [2,4,1,1,3]
result1 = solution.carFleet(target1, position1, speed1)
print(f"Test case 1: {result1}")  # Expected: 3

# Test case 3
target3 = 100
position3 = [0,2,4]
speed3 = [4,2,1]
result3 = solution.carFleet(target3, position3, speed3)
print(f"Test case 3: {result3}")  # Expected: 1

# Test case 4
target4 = 10
position4 = [6,8]
speed4 = [3,2]
result4 = solution.carFleet(target4, position4, speed4)
print(f"Test case 4: {result4}")  # Expected: 2

# Test case 5
target5 = 10
position5 = [8,3,7,4,6,5]
speed5 = [4,4,4,4,4,4]
result5 = solution.carFleet(target5, position5, speed5)
print(f"Test case 5: {result5}")  # Expected: 6

# Test case 6
target6 = 13
position6 = [10,2,5,7,4,6,11]
speed6 = [7,5,10,5,9,4,1]
result6 = solution.carFleet(target6, position6, speed6)
print(f"Test case 6: {result6}")  # Expected: 4
