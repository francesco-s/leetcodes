from collections import defaultdict
from typing import List


class Solution:
    def findWinners(matches: List[List[int]]) -> List[List[int]]:

        players = set()
        losers_count = defaultdict(int)

        for match in matches:
            players.add(match[0])
            players.add(match[1])
            losers_count[match[1]] += 1

        no_losses = [player for player in players if losers_count[player] == 0]
        one_loss = [player for player in players if losers_count[player] == 1]

        return [sorted(no_losses), sorted(one_loss)]


print(Solution.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
