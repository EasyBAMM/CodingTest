# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환!!!
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])   # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


'''
위는 책, 아래 내 코드
match_dict = {')': '('}


def isright(p):
    arr = []
    for s in p:
        if s == '(':
            arr.append(s)
        elif s == ')':
            if len(arr) == 0 or arr[len(arr) - 1] != match_dict[s]:
                return False
            arr.pop()
    if len(arr) != 0:
        return False

    return True


def p2uv(p):
    for i in range(len(p)):
        u = p[:i+1]
        v = p[i+1:]
        # print("u: ", u)
        # print("v: ", v)
        if u.count('(') == u.count(')'):
            # print("count")
            break

    return u, v


def solution(p):
    answer = ''
    if len(p) == 0:  # 빈 문자열
        return answer
    u, v = p2uv(p)
    if isright(u):
        answer = u + solution(v)
    else:
        u = u[1:-1]
        new_u = ''
        for i in range(len(u)):
            if u[i] == '(':
                new_u += ')'
            else:
                new_u += '('
        answer += '(' + solution(v) + ')' + new_u
    return answer


p = input()
print(solution(p))
'''
