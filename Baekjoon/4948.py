n = 123456*2
data = [i for i in range(n+1)]
data[1] = 0

for i in range(2, int(n**0.5)+1):
    if data[i] != 0:
        for j in range(i+i, n+1, i):
            data[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    count = 0

    for i in range(n+1, n*2+1):
        if data[i] != 0:
            count += 1

    print(count)
