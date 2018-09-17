import discord
import pandas as pd
import itertools

# test = [
#     166543497619439618,
#     360081866461806595,
#     324631108731928587,
#     205653475298639872,
#     478080022440181761
# ]


def match(S, Map):
    """マッチング関数。引数はmessage.mentions(list型)、マップ名の文字列"""
    for i in range(5):
        S[i] = "ID:" + str(S[i])
        # S[i] = "ID:" + S[i].id
    df = pd.read_csv("point_" + Map + ".csv", index_col=0)

    if not set(S) <= set(df.index.values):
        return("e1")

    highscore = 0
    ans = []
    P = itertools.permutations(S)
    for p in P: # A,AMID,MID,B,B
        total = 0
        total += int(df.at[p[0], "A"])
        total += (df.at[p[1], "A"]) / 2
        total += (df.at[p[1], "MID"]) / 2
        total += int(df.at[p[2], "MID"])
        total += int(df.at[p[3], "B"])
        total += int(df.at[p[4], "B"])

        if highscore < total:
            highscore = total
            ans = [p]
        elif highscore == total:
            ans.append(p)
    return(ans)


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
#         for y in left4: # AMID選出
#             AMID = [y]
#             left3 = left4[:]
#             left3.remove(y) # MID,AMID以外のメンバー3人のリストを作成
#             for z in left3: # A選出
#                 total = 0
#                 A = [z]
#                 B = left3[:]
#                 B.remove(z) # MID,AMID,A以外のメンバー2人(つまり、Bの2人)のリストを作成
#                 # print(A,AMID,MID,B)
#                 total += int(df.at[A[0], "A"])
#                 total += (int(df.at[AMID[0], "A"]) + int(df.at[AMID[0], "MID"]))/2
#                 total += int(df.at[MID[0], "MID"])
#                 for b_player in B:
#                     total += int(df.at[b_player, "B"])
#                 # print(total)
#                 if highscore < total:
#                     highscore = total
#                     ans = [[A,AMID,MID,B]]
#                 elif highscore == total:
#                     ans.append([A,AMID,MID,B])
#     for x in ans:
#         ansstr.append("【" + map + "】A:" + str(x[0]) + "  AMID:" + str(x[1]) + "  MID:" + str(x[2]) + "  B:" + str(x[3]))
#     return(ansstr)