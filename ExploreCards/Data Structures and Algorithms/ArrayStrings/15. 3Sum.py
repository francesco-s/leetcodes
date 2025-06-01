from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res


# Test cases
solution = Solution()

# Test case 1
nums1 = [-1, 0, 1, 2, -1, -4]
result1 = solution.threeSum(nums1)
print(f"Test case 1: {result1}")  # Expected: [[-1, -1, 2], [-1, 0, 1]] (order may vary)

# You can add more test cases below