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


def countPrimeNumbers(end):
    """Counts the prime numbers between 2 and end"""
    count = 0
    for i in range(2, end + 1):
        if isPrime(i):
            count += 1
    return count


def isWinner(x, nums):
    """Determines who the winner of each game is"""
    wins = {"Ben": 0, "Maria": 0}

    for n in nums:
        if countPrimeNumbers(n) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    return None
