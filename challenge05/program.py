#!/usr/bin/env python3
import sys

CACHE = {}

#5. Recursive Call to Calculate Collatz Cycles
def collatz(n):
    count = 0
    if n <= 1:
        return count
    if n not in CACHE:
        if n % 2 == 0:
            CACHE[n] = collatz(n//2) + 1
        else:
            CACHE[n] = collatz(3 * n + 1) + 1
    return CACHE[n]

if __name__ == '__main__':
    #1. Take Input
    for line in sys.stdin:
        nums = line.split()

        #2. Organize and Potentially Swap Input
        begin = int(nums[0])
        end = int(nums[1])
        swapped = 0

        if end < begin:
            temp = begin
            begin = end
            end = temp
            swapped = 1

        #3. Loop Through Range of Possible Maxes
        maxCyc = 0
        max = 0
        index = begin
        while(index <= end):

            #4. Call Recursive Function
            count = collatz(index)

            #6. Check Max
            if count > max:
                maxCyc = index
                max = count
            index += 1

        #7. Print Max
        if swapped:
            print(end, begin, maxCyc, max + 1)
        else:
            print(begin, end, maxCyc, max + 1)
