c = int(input())
n = 1
level = 1

# 대각선마다의 개수(n), 대각선마다 레벨을 증가시킴(level)
while c > n:
    c = c - n
    n = n + 1
    level = level + 1

# 계산 후 남은 걸로 분수 만듬, 여기서 level 짝수, 홀수로 구분해줌.
if level % 2 == 0:  # 짝수시
    Top = c
    Bottom = level - c + 1
else:  # 홀수시
    Top = level - c + 1
    Bottom = c

answer = str(Top) + "/" + str(Bottom)
print(answer)
