# dfs 어려워,
def dfs(numbers, idx, num, target):
    ret = 0
    if idx == len(numbers):
        if num == target:
            return 1
        else:
            return 0

    ret += dfs(numbers, idx+1, num+numbers[idx], target)
    ret += dfs(numbers, idx+1, num-numbers[idx], target)
    return ret


def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
