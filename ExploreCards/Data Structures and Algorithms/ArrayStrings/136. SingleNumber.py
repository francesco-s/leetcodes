class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = dict()
        res = set()

        for num in nums:
            if num not in seen:
                seen[num] = 1
                res.add(num)
            else:
                seen[num] = 2
                res.remove(num)

        return res.pop()


solution = Solution()

# Test case 1: Single number is 1
nums = [2, 2, 1]
print("Test case 1:", solution.singleNumber(nums))  # Expected output: 1

# Test case 2: Single number is 4
nums = [4, 1, 2, 1, 2]
print("Test case 2:", solution.singleNumber(nums))  # Expected output: 4

# Test case 3: Single number is 0
nums = [0, 1, 1]
print("Test case 3:", solution.singleNumber(nums))  # Expected output: 0

