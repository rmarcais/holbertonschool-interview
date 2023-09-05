#!/usr/bin/python3
"""0. Prime Game"""

def canWin(dp, start):
    """Determines if a player can win"""
    for i in range(start, len(dp)):
        if not dp[i]:
            return True
    return False

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
        dp = [False] * (n + 2)
        dp[0] = True
        dp[len(dp) - 1] = True
        for i in range(1, n + 2):
            if dp[i] and i == n + 1:
                defeats[player] += 1
                player = "Maria"
                break
            if dp[i]:
                continue
            if not isPrime(i) and not canWin(dp, i + 1):
                defeats[player] += 1
                player = "Maria"
                break
            elif not isPrime(i):
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
