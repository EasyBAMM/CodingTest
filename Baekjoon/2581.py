def isprime(num):
    if num < 2:
        return False

    isprime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            isprime = False
            break

    return isprime


m = int(input())
n = int(input())

data = [i for i in range(m, n+1)]

prime_data = []

for x in data:
    if isprime(x):
        prime_data.append(x)

if prime_data:
    sum_prime = sum(prime_data)
    min_prime = min(prime_data)
    print(sum_prime)
    print(min_prime)
else:
    print(-1)
