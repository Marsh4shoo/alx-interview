# test_can_make_total.py

import sys

# Replace '/path/to/your/module' with the actual path where can_make_total.py is located
sys.path.append('/path/to/your/module')

# Correct import of the function from can_make_total module
from can_make_total import can_make_total

def makeChange(coins, total): 
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
    coins = [1, 5, 10, 25]
    total = 63
    print("Minimum coins required:", makeChange(coins, total))


