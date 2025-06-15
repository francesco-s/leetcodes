from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        res = []
        count = 0

        for query in queries:
            count = 0
            for num in nums:
                if num <= query:
                    count += 1
                    query -= num
                else: 
                    break

            res.append(count)
        
        return res

# Test cases
solution = Solution()

# Test case 1
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(f"Test case 1: {solution.answerQueries(nums, queries)}")  # Expected: [2, 3, 4]

# Test case 2
nums = [2, 3, 4, 5]
queries = [1]
print(f"Test case 2: {solution.answerQueries(nums, queries)}")  # Expected: [0]