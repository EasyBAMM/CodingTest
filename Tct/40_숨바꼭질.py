import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
4
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))  # 양방향이면 입력을 추가해줘야함

distance = [INF] * (n+1)
print("before distance: ", distance)
dijkstra(1, graph, distance)
print("after distance: ", distance)

result_a = 0
result_b = 0
result_c = 0
for i in range(1, len(distance)):
    if distance[i] == INF:
        continue
    if result_b < distance[i]:
        result_a = i
        result_b = distance[i]
result_c = distance.count(result_b)
print(result_a, result_b, result_c)
