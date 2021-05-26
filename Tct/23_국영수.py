# https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline

n = int(input())

grades = []

for _ in range(n):
    input_ = input().split()
    input_[1:] = map(int, input_[1:])
    grades.append(input_)


grades = sorted(grades, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in grades:
    print(x[0])


'''
다른사람
import sys
caseCnt = int(input())
arr = []
for i in range(caseCnt):
    name, kor, eng, math = sys.stdin.readline().strip().split()
    arr.append((-int(kor), int(eng), -int(math), name))
arr.sort()
for i in range(len(arr)):
    print(arr[i][3])
'''
