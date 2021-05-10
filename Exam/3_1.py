def solution(n, k, cmd):
    answer = ''
    check = ['O' for i in range(n)]
    delete_row = []
    pos = k

    for c in cmd:
        c = c.split()
        if len(c) > 1:
            action = c[0]
            count = int(c[1])
            if action == "U":
                while True:
                    if pos < 0:
                        pos = 0
                        break
                    if count == 0:
                        break
                    if check[pos] == 'O':
                        count -= 1
                    pos -= 1
            elif action == "D":
                while True:
                    if pos >= n:
                        pos = n - 1
                        break
                    if count == 0:
                        break
                    if check[pos] == 'O':
                        count -= 1
                    pos += 1
        else:
            action = c[0]
            if action == "C":
                delete_row.append(pos)
                check[pos] = 'X'
                temp = pos
                while True:
                    if pos >= n:
                        pos = temp - 1
                        while check[pos] == 'X':
                            pos -= 1
                        break
                    if check[pos] != 'X':
                        break
                    pos += 1
            elif action == "Z":
                check[delete_row.pop()] = 'O'

    answer = ''.join(check)

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
