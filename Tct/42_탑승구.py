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


g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

result = 0
for _ in range(p):
    gi = int(input())
    data = find_parent(parent, gi)
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result += 1

print(result)
