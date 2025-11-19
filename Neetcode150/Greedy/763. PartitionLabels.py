from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Partition string into as many parts so that each letter appears in at most one part.

        TC: O(n) time, where n = len(s)
        SC: O(1) extra space (or O(k) where k = number of unique characters, k <= 26)
        """
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i

        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1

        return res


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "ababcbacadefegdehijhklij"
res1 = solution.partitionLabels(s1)
print(f"Test case 1: {res1}")  # Expected: [9,7,8]

# Test case 2 (example - single partition)
s2 = "eccbbbbdec"
res2 = solution.partitionLabels(s2)
print(f"Test case 2: {res2}")  # Expected: [10]

# Test case 3 (single character)
s3 = "a"
res3 = solution.partitionLabels(s3)
print(f"Test case 3: {res3}")  # Expected: [1]

# Test case 4 (all unique characters)
s4 = "abcdef"
res4 = solution.partitionLabels(s4)
print(f"Test case 4: {res4}")  # Expected: [1,1,1,1,1,1]

# Test case 5 (all same character)
s5 = "aaaaa"
res5 = solution.partitionLabels(s5)
print(f"Test case 5: {res5}")  # Expected: [5]
