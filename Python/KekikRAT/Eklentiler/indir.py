#!/usr/bin/env python
# ! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID

@Client.on_message(Filters.command(['indir'], ['!','.','/']))
def indir(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `indir` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    indirilecekDosya = " ".join(girilenYazi.split()[1:2])

    client.send_document(adminID, indirilecekDosya)

    kekik.edit(mesaj)