class Solution(object):
    def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        pairs = {}

        for num in nums2:
            while stack and num > stack[-1]:
                pairs[stack.pop()] = num
            stack.append(num)

        for el in stack:
            pairs[el] = -1

        return [pairs[num] for num in nums1]
        

    def nextGreaterElementBrute(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(0, len(nums1)):

            for j in range(0, len(nums2)):

                if (nums1[i] == nums2[j]):

                    res.append(-1)
                    for k in range(j + 1, len(nums2)):

                        if nums1[i] < nums2[k]:
                            res[-1] = nums2[k]
                            break

        return res

nums1 = [5,3,1]
nums2 = [3,5,9,3,7,1]

print(Solution.nextGreaterElement(nums1, nums2))

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(Solution.nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]

print(Solution.nextGreaterElement(nums1, nums2))

