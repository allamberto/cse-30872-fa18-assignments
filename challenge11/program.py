#!/usr/bin/env python3
# Collaborated w/ Sean and James

import sys

# Functions

def avoid_kakas(grid, N):

    # Make Min Kakamora Matrix and PathFinding Matrix
    kakas = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    path = [[[0, 0] for _ in range (N + 1)] for _ in range(N + 1)]

    # Fill first column and mark path accordingly
    for i in range(N + 1):
        kakas[i][1] = kakas[i - 1][1] + grid[i][1]
        if  i > 0:
            path[i][1] = [i - 1, 1]

    # Fill first row and mark path accordingly
    for i in range(N + 1):
        kakas[1][i] = kakas[1][i - 1] + grid[1][i]
        if  i > 0:
            path[1][i] = [1, i - 1]

    # first spot in path gets 0
    path[1][1] = [0, 0]

    # Loop through matrices, find min path and mark it in path matrix
    for row in range(2, N + 1):
        for col in range(2, N + 1):
            r = row - 1
            c = col
            if kakas[row][col - 1] < kakas[r][c]:
                r = row
                c = col - 1
            if kakas[row - 1][col - 1] < kakas[r][c]:
                r = row - 1
                c = col - 1

            path[row][col] = [r, c]

            kakas[row][col] = grid[row][col] + min(
                kakas[row][col - 1],
                kakas[row - 1][col - 1],
                kakas[row - 1][col])

    # Now Holds Min Kakamoras
    print(kakas[N][N])

    # Setup Backtracking Process
    node = path[N][N]
    backtrack = [kakas[N][N]]

    if kakas[N][N] != kakas[N][N - 1] and kakas[N][N - 1] == kakas[N - 1][N] or kakas[N][N - 1] == kakas[N - 1][N - 1]:
        node = [N, N - 1]
    elif kakas[N][N] != kakas[N - 1][N] and kakas[N - 1][N] == kakas[N - 1][N - 1]:
        node = [N - 1, N]

    # Backtrack
    while node[0] or node[1]:
        backtrack.append(kakas[node[0]][node[1]])
        node = path[node[0]][node[1]]

    backtrack.reverse()
    return backtrack

# Main Execution
if __name__ == "__main__":

    # Take Input
    N = int(sys.stdin.readline())
    while N != 0:

        # Fill Grid
        grid = [[0 for _ in range(N + 1)]]
        for _ in range(N):
            grid.append([0] + list(map(int, sys.stdin.readline().split())))

        # Dynamic Programming Function
        path = avoid_kakas(grid, N)

        # Print Final Path
        print(path[0], end="")
        for node in range(1, len(path)):
            print(" " + str(path[node] - path[node - 1]), end="")
        print("")

        # Retake Input
        N = int(sys.stdin.readline())
