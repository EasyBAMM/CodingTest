from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0

    distance = 1
    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1


N, M, K, X = map(int, input().split())

visited = [-1] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

bfs(graph, X, visited)

rst = True
for i in range(N+1):
    if visited[i] == K:
        print(i)
        rst = False

if rst:
    print(-1)
