#!/usr/bin/env python3

# Ana Luisa Lamberto

import itertools
import sys
# Functions

def handle_perms():
    result = {}
    perms = [''.join(perm) for perm in itertools.permutations('0123456789')]
    for x in perms:
        num = int(x[:5]) / int(x[5:])
        if num.is_integer():
            result.setdefault(num, [])
            result[num].append(x[:5])
            result[num].append(x[5:])
    return result

# Main execution

if __name__ == '__main__':
    # Fill Perms Dictionary
    result = handle_perms()

    # Take Input
    N = int(sys.stdin.readline())
    loop = True
    while loop:

        # Print Result
        if N in result:
            for i, key in enumerate(result[N]):
                if i % 2:
                    print("/ " + str(key) + " = " + str(N))
                else:
                    print(str(key) + " ", end="")
        else:
            print("There are no solutions for " + str(N) + ".")

        # Retake Input
        N = int(sys.stdin.readline())
        if N != 0:
            print()
        else:
            loop = False
