def factorial(n):
    if n < 2:
        return 1
    answer = 1
    for i in range(2, n+1):
        answer *= i

    return answer


n = int(input())
print(factorial(n))
