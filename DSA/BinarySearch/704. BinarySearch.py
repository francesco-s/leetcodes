class Solution(object):
    def recursive_search(nums, target, left, right):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if left > right:
            return -1
        
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return Solution.recursive_search(nums, target, left, middle - 1)
        else:
            return Solution.recursive_search(nums, target, middle + 1, right)
        
    
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1


        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
        

# Test case 1: Target is in the list
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(f"Test case 1: {Solution.recursive_search(nums, target, 0, len(nums) - 1)}") # Expected Output: 4

# Test case 2: Target is not in the list
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(f"Test case 2: {Solution.recursive_search(nums, target, 0, len(nums) - 1)}")  # Expected Output: -1

# Test case 3: Empty list
nums = []
target = 1
print(f"Test case 3: {Solution.recursive_search(nums, target, 0, len(nums) - 1)}")  # Expected Output: -1

# Test case 4: Single element list, target is present
nums = [5]
target = 5
print(f"Test case 4: {Solution.recursive_search(nums, target, 0, len(nums) - 1)}")  # Expected Output: 0

# Test case 5: Single element list, target is not present
nums = [5]
target = 3
print(f"Test case 5: {Solution.recursive_search(nums, target, 0, len(nums) - 1)}")  # Expected Output: -1


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    left = 0
    right = len(nums) - 1

    while left <= right:
        mean = (left + right) // 2
        if nums[mean] == target:
            return mean
        elif nums[mean] < target:
            left = mean + 1
        else:
            right = mean - 1

