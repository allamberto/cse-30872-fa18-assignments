#!/usr/bin/env python3

import sys
from sympy import *

def findMax(L, W):
    x= Symbol('x')
    V = L * W * x - L * 2 * x ** 2 - W * 2 * x ** 2 + 4 * x ** 3
    deriv = Derivative(V, x)
    expression = deriv.doit()
    return solve(expression, x)[0].evalf()

def findMin(L, W):
    x= Symbol('x')
    V = L * W * x - L * 2 * x ** 2 - W * 2 * x ** 2 + 4 * x ** 3
    deriv = Derivative(V, x)
    expression = deriv.doit()
    return solve(expression, x)[1].evalf()

if __name__ == '__main__':
    for line in sys.stdin:
        L, W = map(int, line.split())
        max = findMax(L, W)
        min = findMin(L, W)
        print('{:.{prec}f} {:.{prec}f}'.format(max, min, prec=3))
