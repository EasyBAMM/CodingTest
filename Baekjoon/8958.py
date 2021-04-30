n = int(input())

testCase = []
for i in range(n):
    testCase.append(input())

for case in testCase:
    sum_case = 0
    num = 0
    for char in case:
        if char == 'O':
            num += 1
        elif char == 'X':
            num = 0
        sum_case += num

    print(sum_case)
