def solution(s):
    answer = len(s)
    n = len(s)

    press = 1
    while press < (n//2+1):
        prev = ''
        new_s = ''
        count = 1
        idx = 0
        while idx <= n:
            next = s[idx:idx+press]
            # print("prev: ", prev, "next: ", next, "count: ", count)
            if prev == next:
                count += 1
            else:
                if count > 1:
                    new_s += (str(count)+prev)
                else:
                    new_s += prev
                count = 1

            prev = next
            idx += press

        if idx > n:
            idx -= press
            new_s += s[idx:]

        answer = min(answer, len(new_s))
        press += 1
        # print(new_s)
    return answer


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))

'''
def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]    # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]    # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer
'''