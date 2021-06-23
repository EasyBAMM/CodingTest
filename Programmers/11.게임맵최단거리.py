from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, mapsize, start, visited):
    n, m = mapsize
    x, y = start
    q = deque([start])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


def solution(maps):

    n = len(maps)
    m = len(maps[0])

    mapsize = (n, m)
    start = (0, 0)
    visited = [[0] * m for _ in range(n)]

    bfs(maps, mapsize, start, visited)

    if visited[n-1][m-1] > 0:
        answer = visited[n-1][m-1]
    else:
        answer = -1

    return answer
