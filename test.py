import numpy as np


def Eratos(n):
    # 에라토스테네스의 체 초기화: n개 요소에 설정
    data = np.arange(n+1)
    data[1] = 0     # 1은 제외, data = [0, 0, 2, 3, 4, ---, n]

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)

    # 제곱근까지 검사
    for i in range(2, m+1):
        # 값이 0이 아니면
        if data[i] > 0:
            data[i+i::i] = 0  # 본인 제외, 소수인 값의 배수를 0으로.

    # 소수 목록 산출(0으로 마스킹한 값 제외)
    return data[data > 0]


print(Eratos(1000))
