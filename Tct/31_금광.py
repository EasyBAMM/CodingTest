t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [[0] * (m+1) for _ in range(n+2)]
    idx = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            graph[i][j] = numbers[idx]
            idx += 1

    print("before graph: ", graph)
    for j in range(1, m+1):
        for i in range(1, n+1):
            graph[i][j] = max(graph[i][j], graph[i-1][j-1] + graph[i][j],
                              graph[i][j-1] + graph[i][j], graph[i+1][j-1] + graph[i][j])

    print("after graph: ", graph)
    result = 0
    for i in range(1, n+1):
        result = max(result, graph[i][m])
    print(result)
