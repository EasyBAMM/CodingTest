n = int(input())
answer = 1

while True:
    if n <= 1:
        break
    n = n - 6*answer
    answer += 1


print(answer)
