from typing import List


class Solution:
    def reverseString2(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(0, len_s // 2):
            backup = s[i]
            s[i] = s[len_s - i - 1]
            s[len_s - i - 1] = backup
        return s

    def reverseString1(s: List[str]) -> None:
        for i in range(0, len(s) // 2):
            s[i], s[-i -1] = s[-i -1], s[i]
        return s
    

    def helper(self, s, left, right):
        if left >= right:
            return
        s[left], s[right - 1] = s[right - 1], s[left]
        self.helper(s, left + 1, right - 1)
        
    def reverseString(self, s: List[str]) -> None:
        return self.helper(s, 0 , len(s))
    
    




# Test cases
solution = Solution()
test_case_1 = ["h", "e", "l", "l", "o"]
solution.reverseString(test_case_1)
print(test_case_1)  # Output: ["o", "l", "l", "e", "h"]

test_case_2 = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(test_case_2)
print(test_case_2)  # Output: ["h", "a", "n", "n", "a", "H"]
