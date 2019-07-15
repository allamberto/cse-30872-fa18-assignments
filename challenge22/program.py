#!/usr/bin/env python3

import sys
CACHE = {}

def findCaleb(sum):
    if sum == 1:
        return 2
    if sum == 2:
        return 5
    if sum == 3:
        return 13
    if sum not in CACHE:
        CACHE[sum] = 2 * findCaleb(sum - 1) + findCaleb(sum - 2) + findCaleb(sum - 3)
    return CACHE[sum]

if __name__ == '__main__':
    for line in sys.stdin:
        print(findCaleb(int(line)))
