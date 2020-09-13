#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import os

@Client.on_message(Filters.command(['islemler'], ['!','.','/']))
def islemler(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `islemler` Komutunu Verdi!\n\n"

    liste = os.popen('tasklist /FI \"STATUS ne NOT RESPONDING\"')
    islemler = ""

    kayit = []

    for eleman in liste:
        eleman.replace('\n\n', '\n')
        if len(eleman.split()) == 6:
            if eleman.split()[0].endswith(".exe") and eleman.split()[0] not in kayit:
                kayit.append(eleman.split()[0])
                islemler += f"`{eleman.split()[0]}`" + "\n"

    mesaj += islemler
    mesaj += f"\nÇalışan Program Sayısı : `{len(islemler.split())}`"

    kekik.edit(mesaj)