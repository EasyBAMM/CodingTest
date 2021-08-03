n = int(input())
rows = [0] * n
result = 0


def adjacent(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x]-rows[i]) == x - i:
            return False
    return True


def dfs(x, n):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            rows[x] = i
            if adjacent(x):
                dfs(x+1, n)


dfs(0, n)

print(result)
