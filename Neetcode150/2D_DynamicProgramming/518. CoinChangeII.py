class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # TC: O(n * amount), where n = len(coins)
        # SC: O(n * amount) for memo table + O(amount) recursion stack

        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)]

            res = 0

            if amount >= coins[i]:
                res += dfs(
                    i, amount - coins[i]
                )  # just i (can use the same coin) -> Take

            res += dfs(i + 1, amount)  # Don't take

            memo[(i, amount)] = res

            return res

        return dfs(0, amount)


# Test cases
solution = Solution()

# Test case 1 (example)
amount1 = 5
coins1 = [1, 2, 5]
res1 = solution.change(amount1, coins1)
print(f"Test case 1: {res1}")  # Expected: 4 (5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1)

# Test case 2 (example)
amount2 = 3
coins2 = [2]
res2 = solution.change(amount2, coins2)
print(f"Test case 2: {res2}")  # Expected: 0 (cannot make 3 with only 2s)

# Test case 3 (example)
amount3 = 10
coins3 = [10]
res3 = solution.change(amount3, coins3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (zero amount)
amount4 = 0
coins4 = [1, 2, 5]
res4 = solution.change(amount4, coins4)
print(f"Test case 4: {res4}")  # Expected: 1 (empty set)

# Test case 5 (multiple combinations)
amount5 = 4
coins5 = [1, 2, 3]
res5 = solution.change(amount5, coins5)
print(f"Test case 5: {res5}")  # Expected: 4 (1+1+1+1, 1+1+2, 1+3, 2+2)

# Test case 6 (order doesn't matter, check for duplicates)
amount6 = 5
coins6 = [1, 2, 5]
# Logic same as Test Case 1, just confirming distinct combinations, not permutations
res6 = solution.change(amount6, coins6)
print(f"Test case 6: {res6}")  # Expected: 4

# Test case 7 (large amount, single coin)
amount7 = 100
coins7 = [1]
res7 = solution.change(amount7, coins7)
print(f"Test case 7: {res7}")  # Expected: 1
