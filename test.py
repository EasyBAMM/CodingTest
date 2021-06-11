import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    q = []
    x, y = 0, 0
    heapq.heappush(q, (graph[x][y], x, y))

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
