#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import os

@Client.on_message(Filters.command(['pwd'], ['!','.','/']))
def pwd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `pwd` Komutunu Verdi!\n\n"

    cwd = os.path.abspath(os.getcwd())

    mesaj += f"{cwd}"
    kekik.edit(mesaj)