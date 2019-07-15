#!/usr/bin/env python3

import sys
import math

# Matrix Manipulation to Find Row and Column
def findRowAndColumn(time):
    diagonal = math.ceil(math.sqrt(int(line)))
    move = diagonal ** 2
    if move % 2:
        if move - time < diagonal:
            r = diagonal
            c = move - time + 1
        else:
            r = time - (diagonal - 1) ** 2
            c = diagonal
    else:
        if move - time < diagonal:
            r = move - time + 1
            c = diagonal
        else:
            r = diagonal
            c = time - (diagonal - 1) ** 2
    return str(r), str(c)

if __name__ == '__main__':
    for line in sys.stdin:
        time = int(line)
        row, column = findRowAndColumn(time)
        print("{} = ({}, {})".format(str(time), row, column))
