#!/usr/bin/env python3

# Ana Luisa Lamberto

import itertools
import sys

# Functions

def decide_Illum(perm, result, position):
    # Recursively Check All Options
    if position == len(perm):
        return result == 13
    return decide_Illum(perm, result + perm[position], position + 1) or decide_Illum(perm, result - perm[position], position + 1) or decide_Illum(perm, result * perm[position], position + 1) or decide_Illum(perm, perm[position] - result, position + 1)

# Main Function
if __name__ == '__main__':
    # Take Input
    for line in sys.stdin:
        tup = [int(t) for t in line.split()]

        # Sort for Perms
        tup.sort()
        result = False

        # Check All Operations of Perms
        for perm in itertools.permutations(tup):
            result = decide_Illum(perm, perm[0], 1)
            if result == True:
                break
        # Return Result
        if result:
            print("Illuminati!")
        else:
            print("Nothing to see")
