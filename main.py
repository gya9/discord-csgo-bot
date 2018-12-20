import sys, discord, requests, json, traceback
import numpy as np
import pandas as pd
from matching import match
from keys import token_str, steamapi_key_str, gya9_id
from func import get_steam_id, edit_id, get_lobby, checkid

class MyClient(discord.Client):
    async def send2developer(self, msg):
        """ 開発者にDMを送る """
        # DEVELOPER_ID に自分のユーザIDを入れてください
        developer = self.get_user(gya9_id)
        dm = await developer.create_dm()
        await dm.send(msg)

    async def on_ready(self):
        """ 起動時のイベントハンドラ """
        msg = f'Logged on as {self.user}!'
        await self.send2developer(msg)

    async def on_message(self, message):
        """ メッセージ受信時のイベントハンドラ """
        try:
            if message.author != self.user: # bot自身の発言には反応しない
                if message.content.startswith("おはよう"):
                    m = "おはようございます、" + message.author.name + "さん！"
                    await message.channel.send(m)

                if message.content.startswith("おやすみ"):
                    m = "おやすみなさい、" + message.author.name + "さん！"
                    await message.channel.send(m)

                if message.content.startswith("!id"):
                    m1 = edit_id(self, message)
                    await message.channel.send(m1)

                if message.content.startswith("!lobby"):
                    msg, flag = get_lobby(self, message)
                    if flag == 1:
                        await message.channel.send(msg)
                    elif flag == 0:
                        # await self.get_channel(524617506992816138).send(msg)
                        await message.channel.send(msg)

                if message.content.startswith("!checkid"):
                    msg, flag = checkid(self, message)
                    await message.channel.send(msg)

                if message.content.startswith("!bye"):
                    m1 = "shutting down"
                    message.channel.send(m1)
                    await self.logout()

        except Exception: # エラー発生時にはトレースバックがDMで送られてくる
            await self.send2developer(traceback.format_exc())

MyClient().run(token_str)