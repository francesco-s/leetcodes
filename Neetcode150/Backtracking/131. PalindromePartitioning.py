from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Time Complexity: O(n * 2^n) - In the worst case, each character can be a partition.
        # Space Complexity: O(n) - Recursion stack depth and temporary substring list.
        res = []

        def is_palindrome(s: str):
            return s == s[::-1]

        def dfs(i, substring):
            if i == len(s):
                res.append(substring[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(s[i : j + 1]):
                    substring.append(s[i : j + 1])
                    dfs(j + 1, substring)
                    substring.pop()

        dfs(0, [])
        return res


# Test cases
solution = Solution()

# Test case 1 (example)
s1 = "aab"
r1 = solution.partition(s1)
print(f"Test case 1: {r1}")  # Expected: [["a","a","b"],["aa","b"]]

# Test case 2 (single char)
s2 = "a"
r2 = solution.partition(s2)
print(f"Test case 2: {r2}")  # Expected: [["a"]]

# Test case 3 (all same letters)
s3 = "aaa"
r3 = solution.partition(s3)
print(f"Test case 3: {r3}")  # Expected: [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]

# Test case 4 (palindrome word)
s4 = "racecar"
r4 = solution.partition(s4)
print(
    f"Test case 4 size: {len(r4)}"
)  # Expected >= 3; includes ["r","a","c","e","c","a","r"], ["r","aceca","r"], ["racecar"]

# Test case 5 (no two-letter palindrome)
s5 = "abc"
r5 = solution.partition(s5)
print(f"Test case 5: {r5}")  # Expected: [["a","b","c"]]

# Test case 6 (mixed palindromes)
s6 = "abbaeae"
r6 = solution.partition(s6)
# Should include splits like ["a","b","b","a","e","a","e"], ["abba","e","a","e"], ["a","bb","a","e","a","e"], ["a","b","b","a","eae"]
print(f"Test case 6 size: {len(r6)}")
