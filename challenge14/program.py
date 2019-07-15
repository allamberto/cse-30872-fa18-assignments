#!/usr/bin/env python3

import sys
count = 0

#Define Node Class
class Node:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None

# Convert Target to Binary
def numToBinary(target):
    # Check for Zero Edge Case
    if target == 0:
        return '0'
    binaryNum = [0] * target

    # Creates Binary Number Backwards with Remainders
    i = 0;
    while (target > 0):
        binaryNum[i] = target % 2;
        target = int(target / 2);
        i += 1;

    # Put Binary Number in Crrect Order
    binaryNum.reverse()

    # Pop Any Zeros Off the Front of Binary Number
    pop = True
    while pop:
        if binaryNum[0] == 0:
            binaryNum.pop(0)
        elif binaryNum[0] == 1:
            pop = False
        if len(binaryNum) < 1:
            binaryNum = 0
            pop = False

    return binaryNum

# Count Total Number of Paths With Binary Recursively
def findPaths(root, binary, path):
    # Make global count available in function
    global count

    # Base Case
    if not root:
        return root

    path.append(root.val)
    findPaths(root.left, binary, path)
    findPaths(root.right, binary, path)

    # Check if Last Part of Current Path Holds Binary Numbers
    if path[len(path) - len(binary):] == binary:
        count += 1
    path.pop()

# Create Tree from Given Array
def buildTree(nodes, root, i):
    if i < len(nodes):
        root = Node(nodes[i]);
        root.left = buildTree(nodes, root.left, 2 * i + 1);
        root.right = buildTree(nodes, root.right, 2 * i + 2);
    return root;

# Level-by-Level Tree Print for Debugging
def BFT(root):
    if not root:
        return
    q = []
    q.append(root)

    #Recurse/Join/Print Through Each Level
    while (len(q) > 0):
        count = len(q)

        #Level Recursion
        level = []
        while count > 0:
            node = q[0]
            level.append(str(node.val))
            q.pop(0)
            if node.left:
                q.append(node.left)
                node.left.parent = node
            if node.right:
                q.append(node.right)
                node.right.parent = node
            count -= 1
        print(" ".join(level))
        level = []

def printResult(target, binary):
    # Make global count available in function
    global count

    print('Paths that form {} in binary ({}): {}'.format(target, binary, count))
    count = 0

if __name__ == "__main__":
    # Take Input
    for line in sys.stdin:
        components = line.split()

        # Check Validity of Input
        if len(components) > 1:
            # Convert Target to Binary
            binary = numToBinary(int(components[0]))

            # Check for Edge Case of Zero As Target
            if components[0] == '0':
                count = 0
                for num in components[1]:
                    if num == '0':
                        count += 1

                # Print Result For Edge Case
                printResult(components[0], "".join(binary))
                continue

            # Build Tree With Given Data
            root = buildTree(list(map(int, components[1])), None, 0)

            # Count Number of Total Paths
            path = []
            findPaths(root, binary, path)

            # Print Result
            printResult(components[0], "".join(list(map(str, binary))))
