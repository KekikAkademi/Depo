#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import webbrowser

@Client.on_message(Filters.command(['url'], ['!','.','/']))
def url(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `url` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    if len(girilenYazi.split()) == 1:
        kekik.edit("Link Vermelisin!")
        return
    link = " ".join(girilenYazi.split()[1:2])

    chromeDizini = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chromeDizini).open(link)

    mesaj += f"`{link}` Adresini Açtım!"

    kekik.edit(mesaj)