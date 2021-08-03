# book - Tct 11장 (그리디 - 곱하기 혹은 더하기)

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


'''
내가 푼 방법
n = input()

sum = 0
for i in n:
    x = int(i)
    if x == 0:
        sum += x
    elif x == 1:
        sum += x
    else:
        if sum == 0:
            sum += x
        else:
            sum *= x

print(sum)
'''
