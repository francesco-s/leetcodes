from collections import Counter, defaultdict


class Solution:

    def canConstruct(ransomNote: str, magazine: str) -> bool:
        count_dict = defaultdict(int)

        for char in magazine:
            count_dict[char] += 1
        for char in ransomNote:
            count_dict[char] -= 1
            if count_dict[char] < 0:
                return False

        return True

    def canConstruct2(ransomNote: str, magazine: str) -> bool:
        diff = Counter(ransomNote) - Counter(magazine)
        return sum(diff.values()) == 0


print(Solution.canConstruct("a", "b"))
print(Solution.canConstruct("aa", "ab"))
print(Solution.canConstruct("aa", "aab"))
