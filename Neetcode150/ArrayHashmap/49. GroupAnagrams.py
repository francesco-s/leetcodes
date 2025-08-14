# LeetCode 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        count_ascii = defaultdict(list)

        for str in strs:
            curr_count = [0] * 26
            for char in str:
                curr_count[ord(char) - ord('a')] += 1

            count_ascii[tuple(curr_count)].append(str)

        return list(count_ascii.values())





# Test cases
solution = Solution()

# Test case 1
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Test case 1: {solution.groupAnagrams(strs1)}")  # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Test case 2
strs2 = [""]
print(f"Test case 2: {solution.groupAnagrams(strs2)}")  # Expected: [[""]]

# Test case 3
strs3 = ["a"]
print(f"Test case 3: {solution.groupAnagrams(strs3)}")  # Expected: [["a"]]

# Test case 4
strs4 = ["abc", "bca", "cab", "xyz"]
print(f"Test case 4: {solution.groupAnagrams(strs4)}")  # Expected: [["abc","bca","cab"],["xyz"]]

# Test case 5
strs5 = ["abbbbbbbbbbb", "aabbbbbbbbbb"]
print(f"Test case 5: {solution.groupAnagrams(strs5)}")  # Expected: [["abbbbbbbbbbb"],["aabbbbbbbbbb"]]
