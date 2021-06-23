# 못 품.
def solution(numbers):

    numbers = list(map(str, numbers))
    n = len(numbers)

    numbers.sort(key=lambda x: (
        x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse=True)

    # print(numbers)
    answer = str(int(''.join(numbers)))

    return answer


'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''
