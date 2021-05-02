n = int(input())

data = list(map(int, input().split()))

count = 0
for x in data:
    isprime = True
    if x < 2:
        continue
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                isprime = False
                break

    if isprime == True:
        count += 1


print(count)
