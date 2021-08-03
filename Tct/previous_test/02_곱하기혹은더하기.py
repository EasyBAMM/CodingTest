def solution():
    answer = 0

    n = input()

    for x in n:
        if int(x) == 0:
            pass
        elif int(x) == 1:
            answer += int(x)
        else:   # inx(x) == number
            if answer == 0:
                answer += int(x)
            elif answer == 1:
                answer += int(x)
            else:
                answer *= int(x)

    return answer


print(solution())
