def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [x for x in range(n)]
edges = []

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

result = 0
total = 0
for edge in edges:
    z, x, y = edge
    total += z
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z

print(total - result)
