#!/usr/bin/python3 
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected output: 5, as [25, 2, 2, 2, 2, 2, 2] is optimal
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1, as no combination can make 1453

