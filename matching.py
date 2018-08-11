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

def choice(SS,df,pos):
    """各ポジションについての最適プレイヤーを選択し、プレイヤー名を返す関数。
       引数はプレイヤーのlist, ポイントのdataframe, 文字列pos("A", "MID", "B")"""
    highscore = -1
    for hito in SS:
        tmp = df.at[hito, pos]
        if tmp > highscore:
            highscore = tmp
            ans = hito
    return(ans)

def match_mirage(S):
    """mirageのマッチング関数。引数はset型"""
    SS = list(S)
    result = [[],[],[]]
    df = pd.read_csv("point_mirage.csv", index_col=0)

    #mid決め
    ans = choice(SS,df,"MID")
    result[1].append(SS.pop(SS.index(ans)))

    #A決め(1位)
    ans = choice(SS,df,"A")
    result[0].append(SS.pop(SS.index(ans)))

    #B決め(1位)
    ans = choice(SS,df,"B")
    result[2].append(SS.pop(SS.index(ans)))

    #A決め(2位)
    ans = choice(SS,df,"A")
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

    #mid決め
    ans = choice(SS,df,"MID")
    result[1].append(SS.pop(SS.index(ans)))

    #A決め(1位)
    ans = choice(SS,df,"A")
    result[0].append(SS.pop(SS.index(ans)))

    #B決め(1位)
    ans = choice(SS,df,"B")
    result[2].append(SS.pop(SS.index(ans)))

    #A決め(2位)
    ans = choice(SS,df,"A")
    result[0].append(SS.pop(SS.index(ans)))

    #B決め(2位)
    result[2].append(SS.pop(0))

    a = result[0]
    mid = result[1]
    b = result[2]

    return("【cache】A:" + str(a) + "  MID:" + str(mid) + "  B:" + str(b))

