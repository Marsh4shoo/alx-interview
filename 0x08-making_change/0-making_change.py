#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total.

:param coins: List of integers representing coin denominations.
:param total: Integer, the total amount to make change for.
:return: Minimum number of coins needed to meet the total, or -1 if not possible.
"""

def makeChange(coins, total):
 
    if total <= 0:
        return 0

    # Initialize an array of size (total + 1) with a large number representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make total 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for each amount that can be reached by the current coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
