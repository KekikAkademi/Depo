#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import os

@Client.on_message(Filters.command(['cd'], ['!','.','/']))
def cd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `cd` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    gidilecekDizin = " ".join(girilenYazi.split()[1:2])
    os.chdir(gidilecekDizin)

    mesaj += f"Şu Şekilde Değişti :\n{os.getcwd()}"
    kekik.edit(mesaj)