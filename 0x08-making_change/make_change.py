def makeChange(coins, total):
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

