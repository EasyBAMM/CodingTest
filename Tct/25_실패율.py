def solution(N, stages):
    result = []
    players = len(stages)

    # 1단계부터 ~ N단계까지
    idx = 1
    while True:
        if idx > N:
            break

        fail_player = stages.count(idx)
        success_player = players
        if fail_player == 0:
            percent_fails = 0
        else:
            percent_fails = fail_player / success_player
        result.append((percent_fails, idx))
        players -= fail_player
        idx += 1

    result.sort(key=lambda x: (-x[0], x[1]))
    result = [x[1] for x in result]
    return(result)


N = 4
stages = [4, 4, 4, 4, 4]
print(solution(N, stages))


'''
기존 코드
def solution(N, stages):
    answer = []
    
    _answer = []
    for i in range(1, N+1):
        add = []
        add.append(i)
        
        playerReach = 0
        playerFail = 0
        percentFail = 0
        
        for j in stages:
            if j >= i:
                playerReach+=1
            
            if j == i:
                playerFail+=1
        
        if playerReach == 0:
            percentFail = 0
        else:
            percentFail =  playerFail / playerReach
        
        add.append(percentFail)
        _answer.append(add)
    
    _answer = sorted(_answer, key = lambda x : (-x[1], x[0]))
    
    answer = [x[0] for x in _answer ]
    
    return answer
'''
