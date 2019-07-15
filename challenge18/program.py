#!/usr/bin/env python3

import sys
import collections


# Graph Structures

Graph = collections.namedtuple('Graph', 'edges degrees')

# Read in 3 Number Pairs and Track Dependencies in Graph
def read_graph():
    edges = collections.defaultdict(set)
    degrees = collections.defaultdict(int)
    visited = []

    for line in sys.stdin:
        input = list(line.rstrip())
        a = input[0]
        b = input[1]
        c = input[2]

        edges[a].add(b)
        edges[b].add(c)
        if (a, b) not in visited:
            degrees[b] += 1
        if (b, c) not in visited:
            degrees[c] += 1
        visited.append((a, b))
        visited.append((b, c))
        degrees[a]

    return Graph(edges, degrees)

# Topological Sort on Graph
def topological_sort(graph):
    frontier = [v for v, d in graph.degrees.items() if d == 0]
    visited = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1
            if graph.degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

if __name__ == '__main__':
    # Take Input
    graph = read_graph()

    # Perform Sort
    ordering = topological_sort(graph)

    # Check for Cycle and Print Result
    if len(ordering) < len(graph.degrees):
        print("Cycle")
    else:
        print("".join(ordering))
