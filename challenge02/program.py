#!/usr/bin/env python3
import sys

import string
import os
import sys

#Functions
def convert(num):
    nums = list(str(num))
    row1 = ""
    row2 = ""
    row3 = ""
    for counter, n in enumerate(nums):
        if n == "-":
            row1 += "   "
            row2 += " _ "
            row3 += "   "
        if n == "1":
            row1 += "   "
            row2 += " | "
            row3 += " | "
            row2 += "  |"
            row3 += "  |"

        if n == "2":
            row1 += " _ "
            row2 += " _|"
            row3 += "|_ "
        if n == "3":
            row1 += " _ "
            row2 += " _|"
            row3 += " _|"
        if n == "4":
            row1 += "   "
            row2 += "|_|"
            row3 += "  |"
        if n == "5":
            row1 += " _ "
            row2 += "|_ "
            row3 += " _|"
        if n == "6":
            row1 += " _ "
            row2 += "|_ "
            row3 += "|_|"
        if n == "7":
            row1 += " _ "
            row2 += "  |"
            row3 += "  |"
        if n == "8":
            row1 += " _ "
            row2 += "|_|"
            row3 += "|_|"
        if n == "9":
            row1 += " _ "
            row2 += "|_|"
            row3 += "  |"
            row3 += " _|"

        if n == "0":
            row1 += " _ "
            row2 += "| |"
            row3 += "|_|"

        if counter < (len(nums) - 1):
            row1 += " "
            row2 += " "
            row3 += " "
    print(row1 + "\n" + row2 + "\n" + row3)

#if __name__ == '__main__':

    print(row1 + "\n" + row2 + "\n" + row3)


for line in sys.stdin:
    line = line.rstrip()
    expression = line.split(" ")
    nums = []
    result = 0

    for op in expression:
        if op == "*":
            if result == 0: #account for multiply by 0
                result = 1
            for num in nums:
                result = num * result
            nums = []
        elif op == "+":
            for num in nums:
                result = num + result
            nums = []
        elif op == "-":
            if result == 0:
                result = nums[0] - nums[1]
            else:
                result = result - nums[0]
            nums = []
        elif op == "/":
            if result == 0:
                result = nums[0]//nums[1]
            else:
                result = result // nums[0]
            nums = []
        elif op == "^":
            if result == 0:
                result = nums[0] ** nums[1]
            else:
                result = result ** nums[0]
            nums = []
        else:
            nums.append(int(op))
    convert(result)

    if len(expression) == 1:
        convert(expression[0])
    else:
        for op in expression:
            if op in "+-/*^":
                if op == "+":
                    result = nums.pop() + nums.pop()
                if op == "-":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    result = num2 - num1
                if op == "/":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    result = num2 // num1
                if op == "*":
                    result = nums.pop() * nums.pop()
                if op == "^":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    result = num2 ** num1
                nums.append(result)
            else:
                nums.append(int(op))
        convert(result)
