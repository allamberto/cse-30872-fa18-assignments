#!/usr/bin/env python3

import sys

def count_legos(legos):
    total = 0
    l = []
    legos.sort(reverse=True)
    insert = True
    for lego in legos:
        if lego == 0:
            continue
        if lego == 4:
            total += 1
            continue
        if len(l) == 0:
            l.append(lego)
            continue
        for i, element in enumerate(l):
            if (element + lego) <= 4:
                insert = False
                l[i] = element + lego
                break
        if insert:
            l.append(lego)
        insert = True

    total += len(l)

    return total

def create_legos(input):
	legos = []
	index = 1
	for lego in input:
		for c in range(lego):
			legos.append(index)
		index += 1
	return legos

if __name__ == "__main__":
	for line in sys.stdin:
		input = [int(lego) for lego in line.rstrip().split()]
		legos = create_legos(input)
		print(count_legos(legos))
