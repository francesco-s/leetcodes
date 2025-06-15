from collections import defaultdict, Counter

class Solution:

    def intersectCounter(self, nums1, nums2):
        return list((Counter(nums1) & Counter(nums2)).elements())
    
    def intersectBrute(self, nums1, nums2):
        i , j = 0, 0
        res = []

        if len(nums1) < len(nums2):
            while i < len(nums1):
                j = 0
                while j < len(nums2):
                    if nums1[i] == nums2[j]:
                        res.append(nums1[i])
                        nums2[j] = -1
                        break
                    j += 1
                i += 1
        else:
            while i < len(nums2):
                j = 0
                while j < len(nums1):
                    if nums2[i] == nums1[j]:
                        res.append(nums2[i])
                        nums1[j] = -1
                        break
                    j += 1
                i += 1
        return res
    
    
    def intersect(self, nums1, nums2):
        """
        Placeholder for the solution to LeetCode 350: Intersection of Two Arrays II.
        """
        nums1_hashmap = defaultdict(int)
        nums2_hashmap = defaultdict(int)

        for num in nums1:
            nums1_hashmap[num] += 1
        for num in nums2:
            nums2_hashmap[num] += 1

        res = []

        for key in nums1_hashmap:
            if key in nums2_hashmap:
                count = min(nums1_hashmap[key], nums2_hashmap[key])
                res.extend(count * [key])
        
        return res

# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = solution.intersect(nums1, nums2)
print(f"Test case 1: {result}")  # Expected: [2, 2]

# Test case 2
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = solution.intersect(nums1, nums2)
print(f"Test case 2: {result}")  # Expected: [4, 9] or [9, 4] (order does not matter)

# Test case 3
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = solution.intersect(nums1, nums2)
print(f"Test case 3: {result}")  # Expected: []

# Test case 4
nums1 = []
nums2 = [1, 2, 3]
result = solution.intersect(nums1, nums2)
print(f"Test case 4: {result}")  # Expected: []

# Test case 5
nums1 = [1, 1, 1, 1]
nums2 = [1, 1]
result = solution.intersect(nums1, nums2)
print(f"Test case 5: {result}")  # Expected: [1, 1]