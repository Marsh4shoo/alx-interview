#!/usr/bin/python3

# test_can_make_total.py

import sys

# Replace '/path/to/your/module' with the actual path where can_make_total.py is located
sys.path.append('/path/to/your/module')

# Correct import of the function from can_make_total module (if needed)
# Uncomment the line below if you have a can_make_total.py module with a can_make_total function.
# from can_make_total import can_make_total

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of the values of the coins in your possession.
    total (int): The total amount to be made.

    Returns:
    int: Minimum number of coins needed to make the total amount, or -1 if it cannot be made.
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Sort coins in descending order to try the largest ones first
    coins.sort(reverse=True)

    # Initialize the counter for coins used
    coin_count = 0

    # Iterate through each coin denomination
    for coin in coins:
        # If the coin can be used, calculate how many times it fits into the remaining total
        if total >= coin:
            coin_count += total // coin  # Add the number of coins used
            total %= coin  # Update the remaining total

        # If the remaining total is zero, return the count of coins used
        if total == 0:
            return coin_count

    # If total is not zero after trying all coins, return -1
    return -1

# Example test case
if __name__ == "__main__":
    # Sample coins and total to test the function
    coins = [1, 5, 10, 25]
    total = 63
    print("Minimum coins required:", makeChange(coins, total))  # Expected output: 6 (25 + 25 + 10 + 1 + 1 + 1)



