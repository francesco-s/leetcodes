from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Find the minimum number of coins needed to make the given amount.
        
        Time Complexity: O(amount * len(coins)) - we compute dp for each amount (0 to amount)
        and for each amount we try all coins
        
        Space Complexity: O(amount) - memo dictionary stores at most amount+1 entries
        """
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            res = 1e10
            for coin in coins:
                diff = amount - coin
                if diff >= 0:
                    res = min(res, 1 + dp(diff))

            memo[amount] = res
            return res

        min_coin = dp(amount)
        return -1 if min_coin >= 1e10 else min_coin



# Test cases
solution = Solution()

# Test case 1 (example)
coins1 = [1,2,5]
amount1 = 11
res1 = solution.coinChange(coins1, amount1)
print(f"Test case 1: {res1}")  # Expected: 3 (5 + 5 + 1)

# Test case 2 (example)
coins2 = [2]
amount2 = 3
res2 = solution.coinChange(coins2, amount2)
print(f"Test case 2: {res2}")  # Expected: -1

# Test case 3 (example)
coins3 = [1]
amount3 = 0
res3 = solution.coinChange(coins3, amount3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (single large coin)
coins4 = [10]
amount4 = 5
res4 = solution.coinChange(coins4, amount4)
print(f"Test case 4: {res4}")  # Expected: -1

# Test case 5 (greedy fails)
coins5 = [1,3,4,5]
amount5 = 7
res5 = solution.coinChange(coins5, amount5)
print(f"Test case 5: {res5}")  # Expected: 2 (3 + 4, greedy would take 5+1+1=3)

# Test case 6 (large amount)
coins6 = [1,2,5]
amount6 = 100
res6 = solution.coinChange(coins6, amount6)
print(f"Test case 6: {res6}")  # Expected: 20

# Test case 7 (multiple ways)
coins7 = [2,5,10,1]
amount7 = 27
res7 = solution.coinChange(coins7, amount7)
print(f"Test case 7: {res7}")  # Expected: 4 (10+10+5+2)
