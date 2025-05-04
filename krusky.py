def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)
    parent[x] = y

def kruskal(edges, n):
    parent = [i for i in range(n)]
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            print(f"{u} - {v}: {w}")
            union(parent, u, v)

# Sample graph (edge list)
edges = [
    (0, 1, 2), (1, 2, 3), (0, 3, 6),
    (1, 3, 8), (1, 4, 5), (2, 4, 7),
    (3, 4, 9)
]

print("\nKruskal's MST:")
kruskal(edges, 5)