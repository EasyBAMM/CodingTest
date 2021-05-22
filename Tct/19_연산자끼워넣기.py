N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v, max_v = 1e9, -1e9


def dfs(i, res, add, sub, mul, div):
    global max_v, min_v
    if i == N:
        max_v = max(res, max_v)
        min_v = min(res, min_v)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)


dfs(1, nums[0], add, sub, mul, div)
print(max_v)
print(min_v)

'''
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
# +, -, *, //
operators = list(map(int, input().split()))
data = []   # 0이 2개, 1이 1개면 data= [0, 0, 1] 이런 식으로 저장.
for i, v in enumerate(operators):
    if operators[i] > 0:
        data.extend([i] * v)
# print("operators: ", data)

result = []
cases = list(permutations(data, N-1))   # 순열로 N-1개 operator 뽑음.
# print("cases: ", cases)
for case in cases:
    calculation = numbers[0]
    for idx, op in enumerate(case):
        if op == 0:  # +
            calculation += numbers[idx+1]
        elif op == 1:   # -
            calculation -= numbers[idx+1]
        elif op == 2:   # *
            calculation *= numbers[idx+1]
        elif op == 3:   # //
            if calculation < 0:
                calculation = - (abs(calculation) // numbers[idx+1])
            else:
                calculation = calculation // numbers[idx+1]
    result.append(calculation)

# print("result: ", result)
# print("max: ", max(result))
# print("min: ", min(result))
print(max(result))
print(min(result))
'''
