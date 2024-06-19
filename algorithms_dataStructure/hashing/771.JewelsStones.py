from collections import Counter


class Solution:
    def numJewelsInStones(jewels: str, stones: str) -> int:
        own_jewels = 0
        count_stones = Counter(stones)

        for jewel in jewels:
            own_jewels += count_stones[jewel]

        return own_jewels


print(Solution.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
print(Solution.numJewelsInStones(jewels="z", stones="ZZ"))
