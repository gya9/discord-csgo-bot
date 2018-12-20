import re, requests, json
import numpy as np
import pandas as pd
from keys import token_str, steamapi_key_str, gya9_id


def get_steam_id(url):
    url = str(url)

    count = 0
    steamid_ans = []
    split = url.split("/")

    if split[3] == "profiles":
        steamid_ans = split[4]

    elif split[3] == "id":
        res = requests.get(url)
        pat = re.compile("\"steamid\":")

        steamid_index = pat.search(str(res.content)).span()[1] + 1

        while True:
            check = str(res.content)[steamid_index + count]
            if check in map(str,range(10)):
                steamid_ans.append(check)
                count +=1
                pass
            else:
                break

    return("".join(steamid_ans))


def edit_id(self,message):
    split = message.content.split()
    searchid = np.int64(message.author.id)

    url_or_id = split[1]

    if url_or_id.startswith("http"):
        steam_id = get_steam_id(url_or_id)
    else:
        steam_id = url_or_id

    df = pd.read_csv("steamid.csv",index_col=0)

    s_bool = (df["discord_id"] == np.int64(message.author.id))

    if s_bool.sum() == 1:
        df.loc[df["discord_id"] == searchid, "steam_id"] = steam_id
        df.to_csv("steamid.csv", encoding='utf-8')
        m1 = "<@{}> さんのsteamidを更新しました".format(message.author.id)

    else:
        s = pd.Series([message.author.id,steam_id], index=df.columns)
        df = df.append(s, ignore_index=True)
        df.to_csv("steamid.csv", encoding='utf-8')
        m1 = "<@{}> さんのsteamidを登録しました".format(message.author.id)

    return m1


def get_lobby(self,message):
    if len(message.content) > 6:
        lobby_message = message.content[7:]
    else:
        lobby_message = ""

    searchid = np.int64(message.author.id)
    df = pd.read_csv("steamid.csv")
    steam_id = df.loc[df["discord_id"] == searchid]["steam_id"].iloc[0]

    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={}&format=csv&steamids={}".format(steamapi_key_str, steam_id)
    res = requests.get(url)
    if str(res) == "<Response [404]>":
        e1 = "エラー:SteamIDが間違っているようです。 !checkid で確認できます"
        return e1,1
    lists = json.loads(res.text)

    if lists["response"]["players"] == []:
        e1 = "エラー:SteamIDが間違っているようです。 !checkid で確認できます"
        return e1,1
    else:
        man = lists["response"]["players"][0]

    steam_name = man["personaname"]
    try:
        steam_lobby_id = man["lobbysteamid"]
    except KeyError:
        e1 = "エラー:CSGOロビーが立っていません。CSGO内で誰かをinviteするとロビーが生成されます"
        return e1,1
    else:
        if lobby_message != "" :
            m1 = "{}さんが参加者を募集しています。「{}」".format(steam_name, lobby_message)
        else:
            m1 = "{}さんが参加者を募集しています。\r".format(steam_name) + \
                 "steam://joinlobby/730/{}/{}".format(steam_lobby_id,steam_id)

        return m1,0