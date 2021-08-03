# book - Tct 기타알고리즘(소수의판별)

# 소수 판별 함수(가장 간단한 방법)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수가 아님
        return True  # 소수임


print(is_prime_number(4))
print(is_prime_number(7))
