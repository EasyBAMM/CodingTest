from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))

choice = list(combinations(data, 2))
print(choice)

last = []
for x in choice:
    x0, x1 = x
    if x0 != x1:
        last.append(x)

print(last)
print(len(last))
