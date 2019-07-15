#!/usr/bin/env python3

import sys

#Define Node Class
class Node:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None

# Divide and Conquer by Recursing on Two Halves of Split Array
def min_BST(nodes):
    if len(nodes) < 1:
        return
    mid = len(nodes) // 2
    node = Node(nodes[mid])
    node.left = min_BST(nodes[:mid])
    node.right = min_BST(nodes[(mid + 1):])
    return node

# Print Level-by-Level Breadth First Traversal
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
            if node.right:
                q.append(node.right)
            count -= 1
        print(" ".join(level))
        level = []

if __name__ == "__main__":
    for line in sys.stdin:
        nodes = [int(num) for num in line.split()]
        root = min_BST(nodes)
        BFT(root)
