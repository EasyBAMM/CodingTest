def ispossible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1:    # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    result = []

    for build in build_frame:
        x, y, a, b = build
        if b == 0:  # 삭제
            result.remove([x, y, a])  # 일단 삭제
            if not ispossible(result):  # 삭제 불가능
                result.append([x, y, a])    # 다시 복구
        elif b == 1:    # 설치
            result.append([x, y, a])    # 일단 설치
            if not ispossible(result):  # 설치 불가능
                result.remove([x, y, a])    # 다시 복구

    return sorted(result)   # 정렬된 결과를 반환


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(n, build_frame))
