#!/usr/bin/env python3
# Citation: Class Example

import sys

# Functions

def sieve(n):
    primes = set(range(2, n + 1))
    for i in range(2, n + 1):
        for m in range(i*2, n + 1, i):
            try:
                primes.remove(m)
            except KeyError:
                pass
    return primes

def findCarNum(n):
    primes = sieve(n)
    if n in primes:
        return False
    for a in range(2, n - 1):
        if pow(a, n, n) != a:
            return False
    return True

# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        num = int(line.rstrip())
        if not findCarNum(num):
            print("{} is normal.".format(num))
        else:
            print("The number {} is a Carmichael number.".format(num))
