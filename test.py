n, m = map(int, input().split())
visited = [False] * n
out = []


def solve(depth, idx, n, m):
    if depth == m:
        print(" ".join(map(str, out)))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, i, n, m)
            visited[i] = False
            out.pop()


solve(0, 0, n, m)
