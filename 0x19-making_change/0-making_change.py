#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given total total
    """

    if total < 1:
        return 0

    
    dp = [-1 for i in range(0, total + 1)]

    for i in coins:
        if i > len(dp) - 1:
            continue
        dp[i] = 1
        for j in range(i + 1, total + 1):
            if dp[j - i] == -1:
                continue
            elif dp[j] == -1:
                dp[j] = dp[j - i] + 1
            else:
                continue
    return dp[total]
