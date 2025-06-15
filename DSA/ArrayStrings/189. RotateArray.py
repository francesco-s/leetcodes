class Solution(object):
    def rotateBestSol(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a

    
    def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # res = []

        # for i in range(-k, 0):
        #     res.append(nums[i])
        
        # for i in range(0, k + 1):
        #     res.append(nums[i])

        size = len(nums)
        nums[:] = nums[size - k :] + nums[: size - k]
            
        return nums
    

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# After calling rotate, nums should be modified to [5, 6, 7, 1, 2, 3, 4].
print(Solution.rotate(nums, k)) # Output: [5, 6, 7, 1, 2, 3, 4]

nums = [-1, -100, 3, 99]
k = 2
# After calling rotate, nums should be modified to [3, 99, -1, -100].
print(Solution.rotate(nums, k)) # Output: [3, 99, -1, -100]