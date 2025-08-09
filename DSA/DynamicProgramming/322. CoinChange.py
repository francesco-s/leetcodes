# Exercise: Coin Change (322) – Medium
# Link: https://leetcode.com/problems/coin-change/



class Solution:
    def coinChange(self, coins, amount): # 3. BOTTOM-UP DP 
        if amount == 0:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != amount + 1 else -1
    
    # 2. Recursion + MEMOIZATION (Top-Down DP)
    def coinChange_memo(coins, amount):
        memo = {}
        
        def helper(remaining):
            # Controlla se già calcolato
            if remaining in memo:
                return memo[remaining]
            
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                result = helper(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, 1 + result)
            
            memo[remaining] = min_coins
            return min_coins
        
        if amount == 0:
            return 0
        
        result = helper(amount)
        return result if result != float('inf') else -1
    
    # 1. Recursion (Time Limit Exceeded)
    def coinChange_recursive(coins, amount):
        def helper(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                result = helper(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, 1 + result)
            
            return min_coins
        
        if amount == 0:
            return 0
        
        result = helper(amount)
        return result if result != float('inf') else -1


# Test cases
solution = Solution()

# Test case 1
coins1 = [1, 2, 5]
amount1 = 11
result1 = solution.coinChange(coins1, amount1)
print(f"Test case 1: {result1}")  # Expected: 3

# Test case 2
coins2 = [2]
amount2 = 3
result2 = solution.coinChange(coins2, amount2)
print(f"Test case 2: {result2}")  # Expected: -1

# Test case 3
coins3 = [1]
amount3 = 0
result3 = solution.coinChange(coins3, amount3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
coins4 = [1]
amount4 = 2
result4 = solution.coinChange(coins4, amount4)
print(f"Test case 4: {result4}")  # Expected: 2

# Test case 5
coins5 = [2, 5, 10, 1]
amount5 = 27
result5 = solution.coinChange(coins5, amount5)
print(f"Test case 5: {result5}")  # Expected: 4
