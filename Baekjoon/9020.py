n = 10000
primenumber = [i for i in range(n+1)]
primenumber[1] = 0
for i in range(2, int(n**0.5)+1):
    if primenumber[i] != 0:
        for j in range(i+i, n+1, i):
            primenumber[j] = 0

testcase = int(input())
testnum = [int(input()) for i in range(testcase)]


for test in testnum:
    AplusB = test
    A = test // 2
    B = A

    while True:
        if primenumber[A] != 0 and primenumber[B] != 0:
            print(A, B)
            break
        else:
            A -= 1
            B += 1
