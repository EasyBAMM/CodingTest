from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0

combine = list(combinations(data, 3))

diff = 1e9
for x in combine:
    sumx = sum(x)
    if sumx <= M:
        temp = M - sumx
        if temp < diff:
            diff = temp
            result = sumx

print(result)
