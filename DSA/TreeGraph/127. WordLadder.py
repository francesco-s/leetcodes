from collections import deque
from typing import List


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        set_wl = set(wordList)
        unique_char_string = set([c for c in ''.join(set_wl)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for char in unique_char_string:
                for i in range(len(beginWord)):
                    neigh = word[:i] + char + word[i + 1:]
                    if neigh not in seen and neigh in set_wl:
                        seen.add(neigh)
                        queue.append((neigh, steps + 1))

        return 0


solution = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = solution.ladderLength(beginWord, endWord, wordList)
print("Test case 1 - Expected: 5, Got:", result)

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]

result = solution.ladderLength(beginWord, endWord, wordList)
print("Test case 2 - Expected: 0, Got:", result)