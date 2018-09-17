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
    """マッチング関数。引数は(ID:数字)という文字列を要素に含むlist、マップ名の文字列"""
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