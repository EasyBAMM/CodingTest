n = int(input())

data = [x for x in range(1001)]
check = [0 for x in range(1001)]
check[1] = 1
for i in range(2, 1001):
    if check[i] == 0 and data[i] % 2 == 0 or data[i] % 3 == 0 or data[i] % 5 == 0:
        for j in range(i, 1001, i):
            check[i] = 1

answer = [data[i] for i in range(1001) if check[i] == 1]
print(answer[n-1])
