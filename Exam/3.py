# timeover

def solution(n, k, cmd):

    answer = ''
    # initial_n = n
    # initial_k = k
    max_len = n
    real_row = [i for i in range(n)]
    delete_row = []

    for c in cmd:
        c = c.split()
        if len(c) > 1:
            action = c[0]
            count = int(c[1])
            if action == "U":
                k -= count
                if k < 0:
                    k = 0
            elif action == "D":
                k += count
                if k > max_len:
                    k = max_len
        else:
            action = c[0]
            if action == "C":
                delete_row.append(real_row[k])
                del real_row[k]
                max_len -= 1
                if k == max_len:
                    k -= 1
            elif action == "Z":
                recover = delete_row.pop()
                if real_row[k] > recover:
                    k += 1
                max_len += 1
                real_row.append(recover)
                real_row.sort()

    print(real_row)

    answer = "X"*n
    answer = list(answer)
    for x in real_row:
        answer[x] = "O"

    answer = "".join(answer)

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
