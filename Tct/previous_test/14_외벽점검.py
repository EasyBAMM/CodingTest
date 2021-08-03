# https://www.youtube.com/watch?v=G-9-_2f5NKQ

import copy
import itertools


def solution(n, weak, dist):
    dst = copy.deepcopy(dist)
    dst.sort(reverse=True)

    # 1명부터 len(dist)명까지
    for i in range(1, len(dst) + 1):
        # weak = [1, 5, 6, 10]
        # 0, 1, 2, 3
        for item in itertools.combinations(range(len(weak)), i):
            # item = (0, 2)
            d = []
            for j in range(i):
                d.append((weak[item[(j+1) % i] - 1] - weak[item[j]] + n) % n)
            # dst = [4, 3, 2, 1]
            d.sort(reverse=True)    # [3, 1]
            rst = True
            for j in range(i):
                if dst[j] < d[j]:
                    rst = False
                    break

            if rst:
                return i

    answer = -1
    return answer
