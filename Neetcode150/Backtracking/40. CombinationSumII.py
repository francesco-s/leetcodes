class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking solution for Combination Sum II.
        
        Time Complexity: O(n * 2^n) in the worst-case scenario, where n is the number of candidates,
        due to the exponential number of recursive calls.
        
        Space Complexity: O(n) for the recursion stack and temporary list storage.
        """
        res = []
        nums_len = len(candidates)
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return

            for j in range(i, nums_len):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    return
                curr.append(candidates[j])
                dfs(j + 1, curr, total + candidates[j])
                curr.pop()

        dfs(0, [], 0)
        return res

# Test cases
solution = Solution()

# Test case 1 (example)
c1 = [10,1,2,7,6,1,5]
t1 = 8
r1 = solution.combinationSum2(c1, t1)
print(f"Test case 1: {r1}")  # Expected: [[1,1,6],[1,2,5],[1,7],[2,6]] in any order

# Test case 2 (example)
c2 = [2,5,2,1,2]
t2 = 5
r2 = solution.combinationSum2(c2, t2)
print(f"Test case 2: {r2}")  # Expected: [[1,2,2],[5]] in any order

# Test case 3 (no solution)
c3 = [2]
t3 = 1
r3 = solution.combinationSum2(c3, t3)
print(f"Test case 3: {r3}")  # Expected: []

# Test case 4 (single candidate equals target once)
c4 = [3,3,3]
t4 = 3
r4 = solution.combinationSum2(c4, t4)
print(f"Test case 4: {r4}")  # Expected: [[3]]

# Test case 5 (handle duplicates carefully)
c5 = [1,1,1,2,2]
t5 = 4
r5 = solution.combinationSum2(c5, t5)
print(f"Test case 5: {r5}")  # Expected: [[1,1,2],[2,2]] in any order

# Test case 6 (larger mix)
c6 = [1,2,3,4,5]
t6 = 7
r6 = solution.combinationSum2(c6, t6)
print(f"Test case 6: {r6}")  # Expected: [[2,5],[3,4],[1,2,4]] in any order
