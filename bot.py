import discord
from matching import point_mirage, point_cache, match_mirage, match_cache
from token import token_data

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

allhito = {"arch", "darknist", "3ple", "gya9", "keshigomu", "toka", "yukiya", "bekutoru"}

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
            m2 = "!match (メンバー)とかいてね！　空白はmatchの後にひとつだけ、メンバーは,で区切り"
            await client.send_message(message.channel, m1)
            await client.send_message(message.channel, m2)

    if message.content.startswith("!match"):
        if client.user != message.author:
            hito = message.content[7:]
            hitoset = set(hito.split(","))

            # if not hitoset <= allhito:
                # error = "エラー：メンバーがおかしいです　入力にミスがあるかも"

            cache = match_cache(hitoset)
            mirage = match_mirage(hitoset)

            # await client.send_message(message.channel, error)
            await client.send_message(message.channel, cache)
            await client.send_message(message.channel, mirage)

client.run(token_data)