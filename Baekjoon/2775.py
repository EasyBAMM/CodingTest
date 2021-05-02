testcase = int(input())
for _ in range(testcase):
    k = int(input())
    n = int(input())

    data = [[1 for row in range(n)] for col in range(k+1)]

    data[0] = [i for i in range(1, n+1)]

    for i in range(1, k+1):
        for j in range(1, n):
            data[i][j] = data[i][j-1] + data[i-1][j]

    print(data[k][n-1])
