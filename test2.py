def match_cache(S):
    """cacheのマッチング関数。引数はset型"""
    SS = list(S)
    result = [[],[],[]]

    # print(SS)

    #mid決め
    highscore = -1
    for hito in SS:
        tmp = point_cache[hito][1]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to mid")
    result[1].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(1位)
    highscore = -1
    for hito in SS:
        tmp = point_cache[hito][0]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    # print(SS)

    #B決め(1位)
    highscore = -1
    for hito in SS:
        tmp = point_cache[hito][2]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to B")
    result[2].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(2位)
    highscore = -1
    for hito in SS:
        tmp = point_cache[hito][0]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    #B決め(2位)
    result[2].append(SS.pop(0))

    return(result)