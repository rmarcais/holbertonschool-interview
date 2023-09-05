#!/usr/bin/python3
"""0. Prime Game"""


def isPrime(n):
    """Determines if a number is prime"""
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False
        return True
    return False


def isWinner(x, nums):
    """Determines who the winner of each game is"""
    defeats = {"Ben": 0, "Maria": 0}
    player = "Maria"

    for n in nums:
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if dp[i]:
                for k in range(i, -4, -1):
                    if not dp[k]:
                        i = k
            if not isPrime(n) and i == n:
                defeats[player] -= 1
                player = "Maria"
                break
            elif not isPrime(n):
                continue
            else:
                dp[i] = True
                for j in range(2 * i, n + 1, i):
                    dp[j] = True
                if player == "Maria":
                    player = "Ben"
                else:
                    player = "Maria"

    if defeats["Maria"] < defeats["Ben"]:
        return "Maria"
    return "Ben"
