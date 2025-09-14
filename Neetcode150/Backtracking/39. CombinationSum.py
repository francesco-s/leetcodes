from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations where the candidate numbers sum to the target.
        
        Time Complexity (TC): Exponential in the worst case (roughly O(2^(target/min_value))).
        Space Complexity (SC): O(target/min_value) for the recursion stack and additional space for output.
        """
        res = []
        nums_len = len(nums)
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return

            for j in range(i, nums_len):
                if nums[j] + total > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return res
                


# Test cases
solution = Solution()

# Test case 1 (example)
c1 = [2,3,6,7]
t1 = 7
r1 = solution.combinationSum(c1, t1)
print(f"Test case 1: {r1}")  # Expected: [[2,2,3],[7]] in any order

# Test case 2 (example)
c2 = [2,3,5]
t2 = 8
r2 = solution.combinationSum(c2, t2)
print(f"Test case 2: {r2}")  # Expected: [[2,2,2,2],[2,3,3],[3,5]] in any order

# Test case 3 (no solution)
c3 = [2]
t3 = 1
r3 = solution.combinationSum(c3, t3)
print(f"Test case 3: {r3}")  # Expected: []

# Test case 4 (single candidate repeated)
c4 = [3]
t4 = 9
r4 = solution.combinationSum(c4, t4)
print(f"Test case 4: {r4}")  # Expected: [[3,3,3]]

# Test case 5 (multiple paths to same sum ensure uniqueness)
c5 = [2,4,6]
t5 = 8
r5 = solution.combinationSum(c5, t5)
print(f"Test case 5: {r5}")  # Expected: [[2,2,4],[2,6],[4,4]] in any order

# Test case 6 (larger target, reuse allowed)
c6 = [2,3,5,7]
t6 = 10
r6 = solution.combinationSum(c6, t6)
print(f"Test case 6: {r6}")  # Expected: [[2,2,2,2,2],[2,2,3,3],[2,3,5],[3,7],[5,5]] in any order
