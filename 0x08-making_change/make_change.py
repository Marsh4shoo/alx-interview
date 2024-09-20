def makeChange(coins, total):
<<<<<<< HEAD
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of the values of the coins in your possession.
    total (int): The total amount to be made.

    Returns:
    int: Minimum number of coins needed to make the total amount, or -1 if it cannot be made.
    """
    if total <= 0:
        return 0

    # Initialize an array with a large number (infinity), as we want to minimize it
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return -1 if it's not possible to make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1


# Test cases to validate the function
if __name__ == "__main__":
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
    print(makeChange([1, 3, 4], 6))                   # Expected output: 2
    print(makeChange([2], 3))                         # Expected output: -1
=======
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
        if total == 0:
            break
    return num_coins if total == 0 else -1

print(makeChange([1, 2, 5], 11))  # Should return 3 (11 = 5 + 5 + 1)
print(makeChange([2], 3))         # Should return -1 (impossible to make 3 with only 2)
print(makeChange([1], 0))         # Should return 0 (0 coins needed for 0 total)
print(makeChange([1, 5, 10, 25], 30))  # Should return 2 (30 = 25 + 5)
>>>>>>> 0af2842a7538931dc1a8967c15ebcde466767de4

-- INSERT --                                                                                                                                                                         2,1           All
