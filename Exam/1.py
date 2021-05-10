def solution(s):

    n2a = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    answer = 0

    n2a = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]

    for n, a in enumerate(n2a):
        s = s.replace(a, str(n))

    answer = int(s)
    return answer


print(solution("one4seveneight"))
