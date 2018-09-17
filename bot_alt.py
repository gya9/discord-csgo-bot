import discord
import pandas as pd
from matching import match
from token_data import token_data_str

client = discord.Client()

myid = "477152129023344640"

Maps = ["cache", "mirage"]


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

        if message.content.startswith("!command"):
            m1 = "コマンド一覧：!add !del !set !search !match"
            m2 = "「!help !add」のように入力すると各コマンドの説明が出ます(未実装)"
            await client.send_message(message.channel, m1)
            await client.send_message(message.channel, m2)

        if message.content.startswith("!help"):
            if "!add" in message.content:
                m1 = "!add <@" + myid + "> 1,0,2,4,4"
                m2 = "という風に入力してください"
                m3 = "@欄には登録するプレイヤーが入ります"

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)
                await client.send_message(message.channel, m3)

            elif "!del" in message.content:
                m1 = "!del <@" + myid + ">"
                m2 = "という風に入力してください"
                m3 = "@欄には削除するプレイヤーが入ります"

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)
                await client.send_message(message.channel, m3)

            elif "!set" in message.content:
                m1 = "!set <@" + myid + "> cache 2,7,1"
                m2 = "という風に入力してください"
                m3 = "@(登録済の名前), (map名), (A,B,MIDの希望度)"
                m4 = "希望度の例1:  10,0,0 ←絶対Aやりたい！"
                m5 = "希望度の例2:  5,0,5 ←MID以外がいい！"
                m6 = "希望度の例3:  0,0,0 ←空いたところに行きます"
                m7 = "3つの希望度の合計は10以内でお願いします"

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)
                await client.send_message(message.channel, m3)
                await client.send_message(message.channel, m4)
                await client.send_message(message.channel, m5)
                await client.send_message(message.channel, m6)
                await client.send_message(message.channel, m7)

            elif "!search" in message.content:
                m1 = "!search <@" + myid + ">"
                m2 = "という風に入力してください"
                m3 = "@欄には検索するプレイヤーが入ります"

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)
                await client.send_message(message.channel, m3)

            elif "!match" in message.content:
                m1 = "!match <@" + myid + "> <@" + myid + "> <@" + myid + \
                        "> <@" + myid + "> <@" + myid + ">"
                m2 = "という風に入力してください"
                m3 = "5つの@欄にはパーティーメンバーが入ります"
                m4 = "登録されたスコアに基づいて、配置を自動で決定します"

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)
                await client.send_message(message.channel, m3)
                await client.send_message(message.channel, m4)

            else:
                m1 = "コマンド一覧：!add !del !set !search !match"
                m2 = "「!help !add」のように入力すると各コマンドの説明が出ます"
                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m2)

        if message.content.startswith("!add"):
            newid = message.mentions[0].id
            idindex = "ID:" + str(newid)
            flag = True

            for Map in Maps:
                df = pd.read_csv("point_" + Map + ".csv", index_col=0)

                if idindex in df.index.values:
                    e1 = "そのIDは既に登録されています！"
                    flag = False
                    await client.send_message(message.channel, e1)
                    break

                else:
                    df.loc[idindex] = [0, 0, 0]
                    df.to_csv("point_" + Map + ".csv", encoding='utf-8')

            if flag:
                m1 = "<@" + newid + "> さんを追加しました"
                await client.send_message(message.channel, m1)

        if message.content.startswith("!del"):
            delid = message.mentions[0].id
            idindex = "ID:" + str(delid)
            flag = True

            for Map in Maps:
                df = pd.read_csv("point_" + Map + ".csv", index_col=0)

                if idindex not in df.index.values:
                    e1 = "そのIDは登録されていません！"
                    flag = False
                    await client.send_message(message.channel, e1)
                    break

                else:
                    df = df.drop(index="ID:" + str(delid))
                    df.to_csv("point_" + Map + ".csv", encoding='utf-8')

            if flag:
                m1 = "<@" + delid + "> さんを削除しました"
                await client.send_message(message.channel, m1)

        if message.content.startswith("!search"):
            searchid = message.mentions[0].id
            idindex = "ID:" + str(searchid)
            flag = True

            mlist = []
            for Map in Maps:
                df = pd.read_csv("point_" + Map + ".csv", index_col=0)

                if idindex not in df.index.values:
                    e1 = "<@" + searchid + "> さんは登録されていません"
                    flag = False
                    await client.send_message(message.channel, e1)
                    break
                else:
                    mlist.append("【" + Map + "】" + str(df.loc[idindex].values))

            if mlist != []:
                m1 = "<@" + searchid + "> さんの登録データ："
                m = " ".join(mlist)

                await client.send_message(message.channel, m1)
                await client.send_message(message.channel, m)

        if message.content.startswith("!set"):
            split = message.content.split()
            Map = split[2]
            point = [int(i) for i in split[3].split(",")]
            setid = message.mentions[0].id
            idindex = "ID:" + str(setid)

            df = pd.read_csv("point_" + Map + ".csv", index_col=0)

            if idindex not in df.index.values:
                em1 = "未登録のプレイヤーです"
                await client.send_message(message.channel, em1)

            elif sum(point) > 10:
                em3 = "3つの数字の合計が10以下になるようにしてください！"
                await client.send_message(message.channel, em3)

            else:
                df.at[idindex, "A"] = point[0]
                df.at[idindex, "MID"] = point[1]
                df.at[idindex, "B"] = point[2]

                df.to_csv("point_" + Map + ".csv", encoding='utf-8')

                m1 = "<@" + setid + "> さんのデータを更新しました"

                await client.send_message(message.channel, m1)

        if message.content.startswith("!match"):
            hito = message.mentions

            if len(hito) != 5:
                error = "エラー：メンバーの数がおかしいです"
                await client.send_message(message.channel, error)

            else:
                posname = ["A: ","AMID: ","MID: ","B: ","B: "]
                for Map in Maps:
                    if match(hito, Map) == "e1":
                        error = "登録されていないメンバーがいます。 「!add」 コマンドからどうぞ"
                        await client.send_message(message.channel, error)
                        break

                    for ans in match(hito, Map):
                        m = []
                        for i in range(5):
                            pos = posname[i]
                            at = "<@" + ans[i][3:] + ">　"
                            m.append(pos + at)
                        mm = m[0] + m[1] + m[2] + m[3] + m[4]
                        await client.send_message(message.channel, mm)

client.run(token_data_str)
