N = int(input())

answer = 0

for i in range(1, N+1):
    N_list = list(map(int, str(i)))
    sum_all = i + sum(N_list)

    if sum_all == N:
        answer = i
        break

print(answer)
