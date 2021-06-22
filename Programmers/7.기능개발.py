def solution(progresses, speeds):
    from collections import deque
    queue = deque()
    answer = []
    n = len(progresses)
    for i in range(n):
        days = 0
        now_progress = progresses[i]
        while now_progress < 100:
            now_progress += speeds[i]
            days += 1
        queue.append(days)

    prev = queue[0]
    count = 0
    while queue:
        now = queue.popleft()
        if now <= prev:
            count += 1
            continue
        else:
            prev = now
            answer.append(count)
            count = 0

    answer.append(count)

    return answer
