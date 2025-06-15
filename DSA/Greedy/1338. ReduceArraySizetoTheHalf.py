from collections import Counter


class Solution:
    def minSetSize(self, arr):
        num_count = Counter(arr)

        half_len = len(arr) // 2
        set_size = 0

        sorted_desc = sorted(num_count.items(), key=lambda item: item[1], reverse=True)

        for key, value in sorted_desc:
            set_size += 1
            half_len -= value
            if half_len <= 0:
                break
        
        return set_size
            


# Test cases
solution = Solution()

# Test case 1
arr1 = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
result1 = solution.minSetSize(arr1)
print(f"Test case 1: {result1}")  # Expected: 2 (one possible expected output)

# Test case 2
arr2 = [7, 7, 7, 7, 7, 7]
result2 = solution.minSetSize(arr2)
print(f"Test case 2: {result2}")  # Expected: 1 (since one removal of 7's removes the entire array)