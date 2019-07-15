#!/usr/bin/env python3

import collections
import sys

# Candy Tuple
Candy = collections.namedtuple('Candy', 'weight yummy')

# Functions

def organize_bag(Bars, maxweight):

    # Create 2D "bag" with Bars(x) v maxweight(y)
    Weights = [[0 for _ in range(maxweight + 1)] for _ in range(len(Bars) + 1)]

    # Organize Bag
    for i in range(len(Bars) + 1):
        for j in range(maxweight + 1):

            # Check if first row or column b/c those are zero
            if i == 0 or j == 0:
                Weights[i][j] = 0

            # If the bar would fit in the bag, take max of next bar and curr bar
            elif Bars[i - 1].weight <= j:
                Weights[i][j] = max(Bars[i - 1].yummy + Weights[i - 1][j - Bars[i - 1].weight], Weights[i - 1][j])

            # If doesn't fit then move on to next bar
            else:
                Weights[i][j] = Weights[i - 1][j]

    # total yummy in last slot
    totYummy = Weights[len(Bars)][maxweight]
    print(totYummy)

    # Backtrack to find bars
    weight = maxweight
    b = len(Bars)
    backtrack = []
    while b > 0 and totYummy > 0:
        if totYummy == Weights[b - 1][weight]:
            b -= 1
            continue
        else:
            backtrack.append(Candy(Bars[b - 1].weight, Bars[b - 1].yummy))
            totYummy = totYummy - Bars[b - 1].yummy
            weight = weight - Bars[b - 1].weight
            b -= 1

    backtrack = sorted(backtrack, key=lambda tup: tup[1])
    backtrack = sorted(backtrack, key=lambda tup: tup[0])
    for bar in backtrack:
        print("{} {}".format(bar.weight, bar.yummy))

# Main execution

if __name__ == '__main__':
    #Take Initial Input

    N = list(map(int, sys.stdin.readline().split()))
    capacity = N[0]
    numBars = N[1]
    while capacity or numBars:
        # Make List of Candy Tuples
        Bars = []
        for _ in range(numBars):
            N = list(map(int, sys.stdin.readline().split()))
            Bars.append(Candy(N[0], N[1]))

        # Call Dynamic Function
        organize_bag(Bars, capacity)

        # Retake Input
        N = list(map(int, sys.stdin.readline().split()))
        capacity = N[0]
        numBars = N[1]
