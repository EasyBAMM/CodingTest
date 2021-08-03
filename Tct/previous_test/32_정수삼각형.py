# https://www.acmicpc.net/problem/1932
import sys
input = sys.stdin.readline

n = int(input())

triangle = [[0] * (n+1) for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        triangle[i][j+1] = v
# print(triangle)
# input End

for i in range(1, n):
    for j in range(1, n+1):
        triangle[i][j] = triangle[i][j] + \
            max(triangle[i-1][j-1], triangle[i-1][j])

result = 0
for j in range(1, n+1):
    result = max(result, triangle[n-1][j])
# print(triangle)
print(result)
