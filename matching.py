import pandas as pd
import itertools

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

def match(S,map):
    """マッチング関数。引数はメンバーのset:S、マップ名の文字列:map"""
    hito = list(S)
    df = pd.read_csv("point_" + map + ".csv", index_col=0)
    highscore = 0
    ans = []
    ansstr = []
    for x in hito: # MID選出
        MID = [x]
        left4 = hito[:]
        left4.remove(x) # MID以外のメンバー4人のリストを作成
        tot = list(itertools.combinations(left4,2)) # 残った4人中2人をAに
        for a2 in tot: 
            total = 0
            a2 = list(a2)
            b2 = list(set(left4) - set(a2)) # Aじゃない2人はBに
            # print(a2,MID,b2)
            for a_player in a2:
                total += int(df.at[a_player, "A"])
            total += int(df.at[MID[0], "MID"])
            for b_player in b2:
                total += int(df.at[b_player, "B"])
            # print(total)
            if highscore < total:
                highscore = total
                ans = [[a2,MID,b2]]
            elif highscore == total:
                ans.append([a2,MID,b2])
    for x in ans:
        ansstr.append("【" + map + "】A:" + str(x[0]) + "  MID:" + str(x[1]) + "  B:" + str(x[2]))
    return(ansstr)