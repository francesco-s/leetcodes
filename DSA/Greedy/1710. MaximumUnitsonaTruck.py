class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        max_units = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for boxType in boxTypes:
            if truckSize > boxType[0]:
                max_units += boxType[0] * boxType[1]
                truckSize -= boxType[0]
            else:
                max_units += truckSize * boxType[1]
                break

        return max_units

# Test cases
solution = Solution()

# Test case 1:
boxTypes1 = [[1, 3], [2, 2], [3, 1]]
truckSize1 = 4
print(f"Test case 1: {solution.maximumUnits(boxTypes1, truckSize1)}")  # Expected: 8

# Test case 2:
boxTypes2 = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize2 = 10
print(f"Test case 2: {solution.maximumUnits(boxTypes2, truckSize2)}")  # Expected: 91