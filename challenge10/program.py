#!/usr/bin/env python3

import sys

def jump_frog(kids):
    final = len(kids) - 1
    i = len(kids) - 1
    while i >= 0:
        if i + kids[i] >= final:
            final = i
        i -= 1
    return final == 0

if __name__ == "__main__":
	for line in sys.stdin:
		kids = [int(kid) for kid in line.rstrip().split()]
		if jump_frog(kids):
			print('Yes')
		else:
			print('No')
