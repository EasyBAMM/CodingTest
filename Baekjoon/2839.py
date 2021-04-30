n = int(input())
a, b = 3, 5

answer = 0

while True:
    if n % 5 == 0:
        answer = answer + (n // 5)
        print(answer)
        break
    n = n - a
    answer += 1
    if n < 0:
        print("-1")
        break
