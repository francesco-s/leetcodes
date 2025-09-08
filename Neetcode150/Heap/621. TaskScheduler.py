from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_heap = [-task for task in freq if task > 0] # Priority queue
        heapify(max_heap)

        time = 0

        while max_heap:
            cycle = n + 1
            store = []
            task_count = 0

            while cycle > 0 and max_heap:
                curr_occ = -heappop(max_heap)
                if curr_occ > 1:
                    store.append(-(curr_occ - 1))
                task_count += 1
                cycle -= 1

            for x in store:
                heappush(max_heap, x)

            time += task_count if not max_heap else n + 1

        return time



# Test cases
solution = Solution()

# Test case 1 (example)
tasks1 = ["A","A","A","B","B","B"]
n1 = 2
res1 = solution.leastInterval(tasks1, n1)
print(f"Test case 1: {res1}")  # Expected: 8

# Test case 2 (no cooldown -> just count tasks)
tasks2 = ["A","A","A","B","B","B"]
n2 = 0
res2 = solution.leastInterval(tasks2, n2)
print(f"Test case 2: {res2}")  # Expected: 6

# Test case 3 (cooldown 1, can interleave perfectly)
tasks3 = ["A","C","A","B","D","B"]
n3 = 1
res3 = solution.leastInterval(tasks3, n3)
print(f"Test case 3: {res3}")  # Expected: 6

# Test case 4 (requires extra idles with larger cooldown)
tasks4 = ["A","A","A","B","B","B"]
n4 = 3
res4 = solution.leastInterval(tasks4, n4)
print(f"Test case 4: {res4}")  # Expected: 10

# Test case 5 (single task repeated)
tasks5 = ["A","A","A","A"]
n5 = 2
res5 = solution.leastInterval(tasks5, n5)
print(f"Test case 5: {res5}")  # Expected: 10  # schedule like A _ _ A _ _ A _ _ A

# Test case 6 (many distinct tasks, cooldown doesn’t matter)
tasks6 = ["A","B","C","D","E","F"]
n6 = 4
res6 = solution.leastInterval(tasks6, n6)
print(f"Test case 6: {res6}")  # Expected: 6
