import pandas as pd

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

def match_mirage(S):
    """mirageのマッチング関数。引数はset型"""
    SS = list(S)
    result = [[],[],[]]
    df = pd.read_csv("point_mirage.csv", index_col=0)
    # print(SS)

    #mid決め
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"MID"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to mid")
    result[1].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(1位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"A"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    # print(SS)

    #B決め(1位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"B"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to B")
    result[2].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(2位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"A"]
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
    df = pd.read_csv("point_cache.csv", index_col=0)
    # print(SS)

    #mid決め
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"MID"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to mid")
    result[1].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(1位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"A"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to A")
    result[0].append(SS.pop(SS.index(ans)))

    # print(SS)

    #B決め(1位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"B"]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    # print("added",ans,"to B")
    result[2].append(SS.pop(SS.index(ans)))

    # print(SS)

    #A決め(2位)
    highscore = -1
    for hito in SS:
        tmp = df.at[hito,"A"]
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
