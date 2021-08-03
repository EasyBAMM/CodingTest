# book - Tct 12장 (구현 - 럭키 스트레이트)
# https://www.acmicpc.net/problem/18406

n = input()
length = len(n)  # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')

'''
내가 푼 방법
n = input()

mid = (0 + len(n)) // 2
a = n[:mid]
b = n[mid:]

sum_a = sum(list(map(int, a)))
sum_b = sum(list(map(int, b)))

if sum_a == sum_b:
    print('LUCKY')
else:
    print('READY')
'''
