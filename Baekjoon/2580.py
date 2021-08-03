# https://claude-u.tistory.com/360
sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_possible(i, j):
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행열 검사
    for k in range(9):
        if sudoku[i][k] in possible:
            possible.remove(sudoku[i][k])
        if sudoku[k][j] in possible:
            possible.remove(sudoku[k][j])

    # 3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in possible:
                possible.remove(sudoku[p][q])
    return possible


flag = False


def dfs(x):
    global flag

    if flag:
        return

    if x == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        (i, j) = zeros[x]
        possible = is_possible(i, j)    # 가능한 숫자

        for num in possible:
            sudoku[i][j] = num  # 가능한 숫자
            dfs(x + 1)  # 다음 0으로
            sudoku[i][j] = 0    # 초기화


dfs(0)
