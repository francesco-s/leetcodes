from typing import List


class Solution:
    def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(0, len_s // 2):
            backup = s[i]
            s[i] = s[len_s - i - 1]
            s[len_s - i - 1] = backup
        print(s)


Solution.reverseString(["h", "e", "l", "l", "o"])
Solution.reverseString(["H", "a", "n", "n", "a", "h"])
