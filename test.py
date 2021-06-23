n = int(input())
_input = input().split()
now_x, now_y = 1, 1

# L, R, U, D

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for go in _input:
    if go == 'L':
        nx = now_x + dx[0]
        ny = now_y + dy[0]
    elif go == 'R':
        nx = now_x + dx[1]
        ny = now_y + dy[1]
    elif go == 'U':
        nx = now_x + dx[2]
        ny = now_y + dy[2]
    elif go == 'D':
        nx = now_x + dx[3]
        ny = now_y + dy[3]

    if nx <= 0 or nx >= n or ny <= 0 or ny >= n:
        continue
    now_x = nx
    now_y = ny

print(now_x, now_y)
