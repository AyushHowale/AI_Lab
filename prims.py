import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_cost += weight
            print(node)
            for neighbor, wt in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (wt, neighbor))

    print("Total cost of MST (Prim's):", total_cost)

# Graph: adjacency list with (neighbor, weight)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

prims(graph, 'A')