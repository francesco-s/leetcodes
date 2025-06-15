from collections import deque
from typing import List


class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for char in 'ACGT':
                for i in range(8):
                    neigh = gene[:i] + char + gene[i + 1:]
                    if neigh not in seen and neigh in bank:
                        seen.add(neigh)
                        queue.append((neigh, steps + 1))

        return -1


solution = Solution()

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]

result = solution.minMutation(startGene, endGene, bank)
print("Test case 1 - Expected: 1, Got:", result)

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

result = solution.minMutation(startGene, endGene, bank)
print("Test case 1 - Expected: 2, Got:", result)
