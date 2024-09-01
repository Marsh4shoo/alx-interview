<<<<<<< HEAD
def makeChange(coins, total):
    # Step 1: Base case checks
    if total <= 0:
        return 0
    
    # Step 2: Initialize a DP array to store minimum coins for each amount
    # Use a high value (infinity) to indicate that the amount is initially not achievable
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to achieve 0 total
    
    # Step 3: Fill the DP array
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                # Step 4: Update DP value for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Step 5: Check if the amount was achievable
    return dp[total] if dp[total] != float('inf') else -1
=======
#!/usr/bin/python3

def makeChange(coins, total):
    # Implementation goes here
>>>>>>> 0af2842a7538931dc1a8967c15ebcde466767de4

