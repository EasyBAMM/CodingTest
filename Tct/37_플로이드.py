import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[1e9] * (n+1) for _ in range(n+1)]

# 자기 자신 0으로 초기화
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], cost)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:  # 자기 자신 0으로 초기화
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == 1e9:
            print(0, end=' ')
        else:
            print(graph[a][b], end=" ")
    print()
