class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # TC: O(n) - each state (i, can_buy) is computed only once due to memoization
        #            there are 2n possible states (n days × 2 boolean values)
        #            each state requires O(1) computation
        # SC: O(n) - memo contains at most 2n entries (n days × 2 states)
        #            recursion call stack can reach O(n) in worst case
        #            so O(n) + O(n) = O(n) total space

        memo = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0

            if (i, can_buy) in memo:
                return memo[(i, can_buy)]

            hold = dfs(i + 1, can_buy)  # hold

            if can_buy:
                memo[(i, can_buy)] = max(dfs(i + 1, False) - prices[i], hold)  # buy
            else:
                memo[(i, can_buy)] = max(
                    dfs(i + 2, True) + prices[i], hold
                )  # sell + cooldown

            return memo[(i, can_buy)]

        return dfs(0, True)


# Test cases
solution = Solution()

# Test case 1 (example)
prices1 = [1, 2, 3, 0, 2]
res1 = solution.maxProfit(prices1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (example - single day)
prices2 = [1]
res2 = solution.maxProfit(prices2)
print(f"Test case 2: {res2}")  # Expected: 0

# Test case 3 (decreasing prices)
prices3 = [5, 4, 3, 2, 1]
res3 = solution.maxProfit(prices3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (two transaction with cooldown)
prices4 = [1, 2, 4]
res4 = solution.maxProfit(prices4)
print(f"Test case 4: {res4}")  # Expected: 3

# Test case 5 (cooldown blocks optimal transaction)
prices5 = [
    1,
    3,
    4,
    0,
    4,
]  # Buy 1, Sell 4 -> Profit 3, Cooldown 0, Buy 4 impossible (wait), End profit 3?
# Or Buy 1, Sell 3 (Profit 2), Cooldown 4, Buy 0, Sell 4 (Profit 4) -> Total 6?
# Wait, price at index 3 is 0.
# Option A: Buy 1 (d0), Sell 4 (d2) -> +3. Cooldown d3. Done. Total 3.
# Option B: Buy 1 (d0), Sell 3 (d1) -> +2. Cooldown d2. Buy 0 (d3), Sell 4 (d4) -> +4. Total 6.
res5 = solution.maxProfit(prices5)
print(f"Test case 5: {res5}")  # Expected: 6

# Test case 6 (empty)
prices6 = []
res6 = solution.maxProfit(prices6)
print(f"Test case 6: {res6}")  # Expected: 0

# Test case 7 (cooldown forced skip)
prices7 = [1, 2, 3, 0, 2]  # Same as example 1
res7 = solution.maxProfit(prices7)
print(f"Test case 7: {res7}")  # Expected: 3
