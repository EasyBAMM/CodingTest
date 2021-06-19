def solution(record):
    firstword = ["Enter", "Leave", "Change"]

    # ex ) user = {"uid1234": ["Muzi", (Enter, 0), (Enter, 1), (Leave, 3)], "uid4567": ["prodo", (Enter, 2), (Leave, 6)]}
    user = {}
    enterIdx = 0
    for s in record:
        # data = word uid nickname
        data = s.split(' ')
        if data[0] == firstword[0]:  # Enter
            if data[1] not in user:  # if not exist
                user[data[1]] = [data[2], (firstword[0], enterIdx)]
            else:   # if exist
                user[data[1]][0] = data[2]  # change name
                user[data[1]].append((firstword[0], enterIdx))
            enterIdx += 1

        elif data[0] == firstword[1]:   # Leave
            user[data[1]].append((firstword[1], enterIdx))
            enterIdx += 1

        elif data[0] == firstword[2]:   # Change
            user[data[1]][0] = data[2]

    answer = [0] * enterIdx

    for value in user.values():
        # value = ["Muzi", (Enter, 0), (Enter, 1), (Leave, 3)]
        name = value[0]
        for i in range(1, len(value)):
            if value[i][0] == firstword[0]:  # Enter
                answer[value[i][1]] = name+"님이 들어왔습니다."
            elif value[i][0] == firstword[1]:   # Leave
                answer[value[i][1]] = name+"님이 나갔습니다."

    return answer


'''
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        # rr = word, uid, nickname
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        # rr = word, uid, nickname
        rr = r.split(' ')
        if rr[0] != 'Change':
            answer.append(namespace[rr[1]] + printer[rr[0]])

    return answer
'''
