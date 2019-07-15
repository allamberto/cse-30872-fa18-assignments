#!/usr/bin/env python3
import collections
import heapq
import sys

nRows = 0
nCols = 0

# Read Graph
def readGraph():
    global nRows, nCols
    graph = collections.defaultdict(set)

    components = sys.stdin.readline().split()
    nRows = int(components[0])
    nCols = int(components[1])
    if not nRows and not nCols:
        return 0, 0, 0

    # Create Matrix
    matrix = []

    for r in range(nRows):
        lst = []
        matrix.append(lst)
        cols = sys.stdin.readline().split()
        for c in cols:
            if c == '0':
                matrix[r].append(True)
            elif c == '1':
                matrix[r].append(False)
            else:
                matrix[r].append(c)

    # Determine Sources and Targets
    targets = []
    source = 0

    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == 'S':
                source = (i, j)
            elif c == 'E':
                targets.append((i, j))
                matrix[i][j] = True

    return matrix, source, targets

# Check Matrix Bounds
def check(row, col):
    global nRows, nCols
    return ((row >= 0) and (row < nRows) and (col >= 0) and (col < nCols))

# Use Dijkstras to Find Cost
def walkGraph(graph, source, target):
    rowNum1 = [-1, 0, 0, 1]
    colNum1 = [0, -1, 1, 0]
    rowNum2 = [-1, -1, 1, 1]
    colNum2 = [-1, 1, -1, 1]

    frontier = [(0, source, source)]
    visited = {}

    while frontier:
        cost, fr, to = heapq.heappop(frontier)
        if to in visited:
            continue

        visited[to] = fr

        if to == target:
            return visited, cost

        # Push From Each Direction to Frontier
        for i in range(4):
            # Diagonals

            row = to[0] + rowNum2[i]
            col = to[1] + colNum2[i]

            if check(row, col) and graph[row][col]:
                if (row, col) == target:
                    visited[(row, col)] = to
                    return visited, cost + 2
                heapq.heappush(frontier, (cost + 2, to, (row, col)))

            # Horizontal/Vertical

            row = to[0] + rowNum1[i]
            col = to[1] + colNum1[i]

            if check(row, col) and graph[row][col]:
                if (row, col) == target:
                    visited[(row, col)] = to
                    return visited, cost + 1
                heapq.heappush(frontier, (cost + 1, to, (row, col)))

    # Return -1 if not found
    return None, -1

# Recontstruct Path from Visited
def reconstructPath(source, target, visited):
    global nCols
    curr = target
    path = []

    while curr != source:
        # append ID using equation
        path.append(curr[0] * nCols + curr[1])
        curr = visited[curr]

    path.append(source[0] * nCols + source[1])
    path.reverse()

    return path


if __name__ == "__main__":
    while True:
        graph, source, targets = readGraph()

        # Check Termination Cases
        if not graph and not source and not targets:
            break

        if not source:
            print('Cost: 0 Path: None')
            continue

        minPath = 10000
        path = []
        ans = []

        # Check Path for Each Target
        for target in targets:
            visited, cost = walkGraph(graph, source, target)

            # If Not Possible and No Other Solutions Return None
            if cost == -1:
                if len(ans) < 1:
                    minPath = 10000

            # If Shortest Reconstruct Path
            elif cost < minPath:
                path = reconstructPath(source, target, visited)
                ans.append(path)
                minPath = cost

        # Check if Not Possible and Return None Value
        if minPath == 10000:
            print('Cost: 0 Path: None')
            continue

        # Print Final Answer
        print('Cost: {} Path: {}'.format(str(minPath), " ".join(map(str,path))))
