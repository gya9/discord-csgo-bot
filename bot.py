import discord
import pandas as pd
from matching import match
from token_data import token_data_str

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

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

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

    if message.content.startswith("!help"):
        if client.user != message.author:
            m1 = "メンバー一覧:"+str(allhito)
            m2 = "!match (メンバー)：メンバーに応じて自動で配置します。空白はmatchの後にひとつだけ、メンバーは,で区切り"
            m3 = "!set (あなたの名前) (マップ名) (ポイント振り分け) ：A,MID,Bの「行きたい度」を設定します。"
            m4 = "例：!set gya9 mirage 0,3,2"

            await client.send_message(message.channel, m1)
            await client.send_message(message.channel, m2)
            await client.send_message(message.channel, m3)
            await client.send_message(message.channel, m4)

    if message.content.startswith("!match"):
        if client.user != message.author:
            hito = message.content.split()[1]
            hitoset = set(hito.split(","))

            if not hitoset <= allhito:
                error = "エラー：メンバーがおかしいです　入力にミスがあるかも"
                await client.send_message(message.channel, error)

            else:
                for ans_cache in match(hitoset,"cache"):
                    await client.send_message(message.channel, ans_cache)
                for ans_mirage in match(hitoset,"mirage"):
                    await client.send_message(message.channel, ans_mirage)

    if message.content.startswith("!set"):
        if client.user != message.author:
            split = message.content.split()
            point = [int (i) for i in split[3].split(",")]

            if sum(point) > 10:
                em = "3つの数字の合計が10以下になるようにしてください！"
                await client.send_message(message.channel, em)

            else:
                df = pd.read_csv("point_"+ split[2] +".csv", index_col=0)

                df.at[split[1],"A"] = point[0]
                df.at[split[1],"MID"] = point[1]
                df.at[split[1],"B"] = point[2]

                df.to_csv("point_"+ split[2] +".csv", encoding='utf-8')
                await client.send_message(message.channel, df)


client.run(token_data_str)
