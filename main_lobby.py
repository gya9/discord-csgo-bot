import sys, discord, requests, json, steam
import numpy as np
import pandas as pd
from matching import match
from keys import token_data_str, key_data_str
from steamid import get_steam_id

client = discord.Client()

myid = "477152129023344640"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith("おはよう"):
            m = "おはようございます、" + message.author.name + "さん！"
            await client.send_message(message.channel, m)

        if message.content.startswith("おやすみ"):
            m = "おやすみなさい、" + message.author.name + "さん！"
            await client.send_message(message.channel, m)

        if message.content.startswith("!id"):
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
                m1 = "<@" + message.author.id + "> さんのsteamidを更新しました"

            else:
                s = pd.Series([message.author.id,steam_id], index=df.columns)
                df = df.append(s, ignore_index=True)
                df.to_csv("steamid.csv", encoding='utf-8')
                m1 = "<@" + message.author.id + "> さんのsteamidを登録しました"

            await client.send_message(message.channel, m1)

        if message.content.startswith("!lobby"):
            split = message.content.split()

            if len(message.content) > 6:
                lobby_message = message.content[7:]
            else:
                lobby_message = ""

            searchid = np.int64(message.author.id)
            df = pd.read_csv("steamid.csv")
            steam_id = df.loc[df["discord_id"] == searchid]["steam_id"].iloc[0]

            url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={}&format=csv&steamids={}".format(key_data_str, steam_id)
            res = requests.get(url)
            if str(res) == "<Response [404]>":
                e1 = "エラー:SteamIDが間違っているようです。 !checkid で確認できます"
                await client.send_message(message.channel, e1)

            lists = json.loads(res.text)
            man = lists["response"]["players"][0]

            steam_name = man["personaname"]
            try:
                steam_lobby_id = man["lobbysteamid"]
            except KeyError:
                e1 = "エラー:CSGOロビーが立っていません。CSGO内で誰かをinviteするとロビーが生成されます"
                await client.send_message(message.channel, e1)
            else:
                if lobby_message != "" :
                    m1 = "{}さんが参加者を募集しています。「{}」".format(steam_name, lobby_message)
                else:
                    m1 = "{}さんが参加者を募集しています。".format(steam_name)
                m2 = "steam://joinlobby/730/{}/{}".format(steam_lobby_id,steam_id)

                await client.send_message(client.get_channel("524617506992816138"), m1)
                await client.send_message(client.get_channel("524617506992816138"), m2)

        if message.content.startswith("!checkid"):
            df = pd.read_csv("steamid.csv")
            searchid = np.int64(message.author.id)
            steam_id = df[df["discord_id"] == searchid]["steam_id"].iloc[0]

            m1 = "<@{}> さんの登録SteamID:{}".format(message.author.id, steam_id)
            await client.send_message(message.channel, m1)

client.run(token_data_str)
