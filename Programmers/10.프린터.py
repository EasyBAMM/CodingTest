def solution(priorities, location):
    from collections import deque

    print_count = 0
    priorities = list(map(lambda x: [x, 0], priorities))
    priorities[location][1] = "this"
    q = deque(priorities)
    while q:
        J = q.popleft()

        isok = True
        for x in q:
            if x[0] > J[0]:
                isok = False
                break

        if isok:
            print_count += 1
            if J[1] == "this":
                break
        else:
            q.append(J)

    return print_count


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))

'''
from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([v,i] for i, v in enumerate(priorities))
    
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
'''
