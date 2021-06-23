def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=lambda x: len(x))

    for x in s:
        data = x.split(',')
        for j in data:
            if j not in answer:
                answer.append(j)

    answer = list(map(int, answer))
    return answer
