def solution(s):
    answer = len(s)
    n = len(s)
    press = 1

    while press < (n//2+1):  # 압축은 문자열의 크기 절반까지
        result = ''
        prev = ''
        count = 1
        for i in range(0, n, press):
            now = s[i:i+press]
            if prev == now:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += prev
                count = 1
                prev = now

        if count > 1:   # 나머지도 출력해줘야됨
            result += str(count)
        result += now

        print(result)
        answer = min(answer, len(result))
        press += 1

    return answer


s = "xababcdcdababcdcd"
print(solution(s))
