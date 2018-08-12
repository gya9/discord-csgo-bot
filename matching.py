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

# def match(S,map):
#     """マッチング関数。引数はメンバーのset:S、マップ名の文字列:map"""
#     hito = list(S)
#     df = pd.read_csv("point_" + map + ".csv", index_col=0)
#     highscore = 0
#     ans = []
#     ansstr = []
#     for x in hito: # MID選出
#         MID = [x]
#         left4 = hito[:]
#         left4.remove(x) # MID以外のメンバー4人のリストを作成
#         tot = list(itertools.combinations(left4,2)) # 残った4人中2人をAに
#         for a2 in tot: 
#             total = 0
#             a2 = list(a2)
#             b2 = list(set(left4) - set(a2)) # Aじゃない2人はBに
#             # print(a2,MID,b2)
#             for a_player in a2:
#                 total += int(df.at[a_player, "A"])
#             total += int(df.at[MID[0], "MID"])
#             for b_player in b2:
#                 total += int(df.at[b_player, "B"])
#             # print(total)
#             if highscore < total:
#                 highscore = total
#                 ans = [[a2,MID,b2]]
#             elif highscore == total:
#                 ans.append([a2,MID,b2])
#     for x in ans:
#         ansstr.append("【" + map + "】A:" + str(x[0]) + "  MID:" + str(x[1]) + "  B:" + str(x[2]))
#     return(ansstr)

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
        for y in left4: # AMID選出
            AMID = [y]
            left3 = left4[:]
            left3.remove(y) # MID,AMID以外のメンバー3人のリストを作成
            for z in left3: # A選出
                total = 0
                A = [z]
                B = left3[:]
                B.remove(z) # MID,AMID,A以外のメンバー2人(つまり、Bの2人)のリストを作成
                # print(A,AMID,MID,B)
                total += int(df.at[A[0], "A"])
                total += (int(df.at[AMID[0], "A"]) + int(df.at[AMID[0], "MID"]))/2
                total += int(df.at[MID[0], "MID"])
                for b_player in B:
                    total += int(df.at[b_player, "B"])
                # print(total)
                if highscore < total:
                    highscore = total
                    ans = [[A,AMID,MID,B]]
                elif highscore == total:
                    ans.append([A,AMID,MID,B])
    for x in ans:
        ansstr.append("【" + map + "】A:" + str(x[0]) + "  AMID:" + str(x[1]) + "  MID:" + str(x[2]) + "  B:" + str(x[3]))
    return(ansstr)