#!/usr/bin/env python3
import collections
import sys

# Read Graph

def read_graph():

    # read edges
    graph = {}

    components = sys.stdin.readline().rstrip().split()

    temp = []
    while components[0] != '%':
        temp.append(components)
        components = sys.stdin.readline().rstrip().split()

    temp.sort(key=lambda x: x[0])

    for item in temp:
        source, target = map(int, item)
        if source not in graph:
            graph[source] = []
        if target not in graph:
            graph[target] = []
        graph[source].append(target)
        graph[target].append(source)

    return graph

#Find Circuit
def find_circuit(graph, start, vertex, visited, path):
    '''Recursively perform DFS traversal until we reach start'''

    # Base Case: Reach Starting Positions
    if path and vertex == start:
        return path

    # Recursively Visit Each Unvisited edge
    for neighbor in sorted(graph[vertex]):
        if len(path) == len(graph) - 1 and neighbor == start:
            visited.add(vertex)
            path.append((vertex, neighbor))
            return path

        if neighbor in visited:
            continue

        # Take edge and path
        visited.add(neighbor)
        path.append((vertex, neighbor))

        if find_circuit(graph, start, neighbor, visited, path):
            return path

        # Backtrack by removing previous work
        path.pop(-1)
        visited.remove(neighbor)

    return None

# Find Hamilitonian Cycle
def find_ham_cycle(graph):
    '''Iteratively Compute Subciruit Until All Edges Have Been Traversed or No Circuit Possible'''
    start = list(graph.keys())[0]
    visited = set()
    circuit = []
    index = 0

    visited.add(start)

    while start:
        path = find_circuit(graph, start, start, visited, [])
        if not path:
            return None
        circuit = circuit[:index] + path + circuit[index:]

        start = None
        for index, vertex in enumerate(source for source, target in circuit):
            for neighbor in graph.keys():
                if neighbor not in visited:
                    start = vertex
                    break
    return circuit

if __name__ == "__main__":
    while sys.stdin.readline().rstrip():
        graph = read_graph()

        circuit = find_ham_cycle(graph)
        if not circuit:
            print("None")
        else:
            lst = [circuit[0][0]]
            for source, target in circuit:
                lst.append(target)
            print(" ".join(list(map(str, lst))))
