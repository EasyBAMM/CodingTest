# book - Tct 6장
n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data = sorted(data, reverse=True)

for i in data:
    print(i, end=' ')
