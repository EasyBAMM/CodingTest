from itertools import combinations

n = int(input())
data = list(map(int, input().split()))

all_money = []
for i in range(1, n+1):
    money = list(combinations(data, i))
    print(money)
    for x in money:
        if sum(x) not in all_money:
            all_money.append(sum(x))

all_money.sort()


result = 1
idx = 0
while idx < len(all_money):
    if all_money[idx] != result:
        break
    result += 1
    idx += 1

print(all_money)
print(result)


'''
coin_num = int(input())
coin_list = list(map(int, input().split(" ")))

coin_list.sort()

target = 1

for i in coin_list:
    if target < i:
        break
    target += i

print(target)

'''
