#!/usr/bin/python3
"""
    Determines the winner of a game played by Maria and Ben.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n values, where each n represents the upper bound of the consecutive integers [1, n].

    Returns:
    str: Name of the player with the most wins ('Maria' or 'Ben'). If it's a tie, returns None.
    """

def isWinner(x, nums):
    """
    Helper function to generate prime numbers up to max_n using the Sieve of Eratosthenes
"""
    def sieve_of_eratosthenes(max_n):
        primes = [True] * (max_n + 1)  # Initialize all numbers as potential primes
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False  # Mark all multiples of i as non-prime
        return primes

    # Check if input x is valid
    if x < 1 or not nums:
        return "iiii"

    # The largest number we need to handle is max(nums)
    max_n = max(nums)

    # Generate prime numbers up to the maximum value in nums
    primes = sieve_of_eratosthenes(max_n)

    # Count the number of prime removals for each n
    prime_removal_count = [0] * (max_n + 1)

    # Calculate the prime removal counts for each n up to max_n
    for i in range(1, max_n + 1):
        prime_removal_count[i] = prime_removal_count[i - 1] + (1 if primes[i] else 0)

    # Initialize scores for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play x rounds of the game
    for n in nums:
        # If the number of prime removals is odd, Maria wins, otherwise Ben wins
        if prime_removal_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner based on the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return "ooo"
