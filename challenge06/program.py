#!/usr/bin/env python3
import sys

def make_ordered_set(f):
    options = []
    seq = []

    #4. Check for Edge Case of Length 1
    if len(f) == 1:
        return f

    #5. Create Each Possible Set
    for i in range(len(f)):
        j = i
        while(j < len(f)):
            if f[j] not in seq:
                seq.append(f[j])
                j += 1
            else:
                options.append(seq)
                seq = []
                break;

    #6. Check Lengths of Sets
    result = []
    for list in options:
        if len(list) > len(result):
            result = list

    #7. Return Longest Set
    return result

if __name__ == "__main__":
    #1. Input
    for line in sys.stdin:
        line = line.rstrip()
        fruits = line.split()

        #2. Create Set
        set = make_ordered_set(fruits)

        #3. Print Result
        result = ", ".join(set)
        print("{}: {}".format(len(set), result))
