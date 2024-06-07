from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_array = []
    # if nums1 and nums2 and max(nums1) < min(nums2):
    #     merged_array = nums1 + nums2
    # elif nums1 and nums2 and max(nums2) < min(nums1):
    #     merged_array = nums2 + nums1
    # else:

    i, j = 0, 0
    # Traverse both arrays and merge them
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1
        else:
            merged_array.append(nums2[j])
            j += 1

    # If there are remaining elements in arr1, add them to merged_array
    while i < len(nums1):
        merged_array.append(nums1[i])
        i += 1

    # same for arr2
    while j < len(nums2):
        merged_array.append(nums2[j])
        j += 1

    n = len(merged_array)

    if n % 2 == 1:
        return merged_array[n // 2]
    else:
        return (merged_array[(n // 2) - 1] + merged_array[n // 2]) / 2.0


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
print(findMedianSortedArrays([], [1]))
