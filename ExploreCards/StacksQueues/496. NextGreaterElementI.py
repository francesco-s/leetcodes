from collections import defaultdict
from typing import List


# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
#
# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution:

    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:

        found = False
        found_greater = False
        res = []
        already_check = defaultdict(int)

        for num1 in nums1:
            if num1 not in already_check.keys():
                for num2 in nums2:
                    if num2 == num1:
                        found = True
                    elif num2 > num1 and found:
                        already_check[num1] = num2
                        res.append(num2)
                        found_greater = True
                        break
                if not found_greater:
                    already_check[num1] = -1
                    res.append(-1)
                found_greater = False
                found = False
            else:
                res.append(already_check[num1])

        return res

    def nextGreaterElement2(nums1: List[int], nums2: List[int]) -> List[int]:
        found = False
        found_greater = False
        res = []

        for num1 in nums1:
            for num2 in nums2:
                if num2 == num1:
                    found = True
                elif num2 > num1 and found:
                    res.append(num2)
                    found_greater = True
                    break
            if not found_greater:
                res.append(-1)

            found_greater = False
            found = False

        return res


print(Solution.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(Solution.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
print(Solution.nextGreaterElement(nums1=[1, 3, 5, 2, 4], nums2=[5, 4, 3, 2, 1]))
