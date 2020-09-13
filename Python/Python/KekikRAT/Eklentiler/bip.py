#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import winsound, random

@Client.on_message(Filters.command(['bip'], ['!','.','/']))
def bip(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `bip` Komutunu Verdi!\n\n"

    for i in range(1, 5):
        winsound.Beep(random.randint(57, 767), 1000)

    mesaj += "Hallettim !"
    kekik.edit(mesaj)