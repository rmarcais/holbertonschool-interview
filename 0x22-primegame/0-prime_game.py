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
        for i in range(1, n + 1):
            if not isPrime(n) and i == n:
                defeats[player] -= 1
                player = "Maria"
                break
            elif not isPrime(n):
                continue
            else:
                if player == "Maria":
                    player = "Ben"
                else:
                    player = "Maria"

    if defeats["Maria"] < defeats["Ben"]:
        return "Maria"
    return "Ben"
