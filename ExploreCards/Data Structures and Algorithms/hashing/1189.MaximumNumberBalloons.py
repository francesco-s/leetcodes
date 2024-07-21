# Example 1:
#
# Input: text = "nlaebolko"
# Output: 1
#
# Example 2:
#
# Input: text = "loonbalxballpoon"
# Output: 2

from collections import Counter, defaultdict


class Solution:
    def maxNumberOfBalloons(text: str) -> int:
        word_count = defaultdict(int)

        for char in text:
            if char in ['b', 'a', 'l', 'o', 'n']:
                word_count[char] += 1

        word_count['l'] //= 2
        word_count['o'] //= 2

        return min(word_count['b'], min(word_count['a'], min(word_count['l'], min(word_count['o'], word_count['n']))))

    def maxNumberOfBalloons2(text: str) -> int:

        balloon_count = Counter({'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1})
        word_count = Counter(text)

        past_sum, current_sum, nums_balloon = 0, 0, 0

        while True:
            past_sum = sum(word_count.values())
            word_count -= balloon_count
            current_sum = sum(word_count.values())
            if current_sum == past_sum - 7:
                nums_balloon += 1
            else:
                break

        return nums_balloon


print(Solution.maxNumberOfBalloons("nlaebolko"))
print(Solution.maxNumberOfBalloons("loonbalxballpoon"))
print(Solution.maxNumberOfBalloons("leetcode"))
