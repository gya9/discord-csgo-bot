allhito = {
    "arch",
    "darknist",
    "3ple",
    "gya9",
    "keshigomu",
    "toka",
    "yukiya",
    "bekutoru"
    }

point_cache = {
    "arch":[1,3,1],
    "darknist":[5,0,0],
    "3ple":[0,0,5],
    "gya9":[1,3,1],
    "keshigomu":[4,1,0],
    "toka":[1,1,3],
    "yukiya":[2,0,3],
    "bekutoru":[1,2,1],
    }

point_mirage = {
    "arch":[1,3,1],\
    "darknist":[0,0,5],\
    "3ple":[4,0,1],\
    "gya9":[1,4,0],\
    "keshigomu":[0,0,5],\
    "toka":[3,0,2],\
    "yukiya":[0,2,3],\
    "bekutoru":[1,2,2],\
    }

def match_mirage(S):
    """mirageのマッチング関数。引数はset型"""
    SS = list(S)
    result = [[],[],[]]

    # print(SS)

    #mid決め
    highscore = -1
    for hito in SS:
        tmp = point_mirage[hito][1]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to mid")
    result[1].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(1位)
    highscore = -1
    for hito in SS:
        tmp = point_mirage[hito][0]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    # print(SS)

    #B決め(1位)
    highscore = -1
    for hito in SS:
        tmp = point_mirage[hito][2]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to B")
    result[2].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(2位)
    highscore = -1
    for hito in SS:
        tmp = point_mirage[hito][0]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    #B決め(2位)
    result[2].append(SS.pop(0))

    a = result[0]
    mid = result[1]
    b = result[2]

    return("【mirage】A:" + str(a) + "  MID:" + str(mid) + "  B:" + str(b))

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

    a = result[0]
    mid = result[1]
    b = result[2]

    return("【cache】A:" + str(a) + "  MID:" + str(mid) + "  B:" + str(b))
