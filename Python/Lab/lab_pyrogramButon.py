#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from os import listdir

KekikRAT = Client(
    api_id=xxxxx,                                  # my.telegram.org/apps
    api_hash="xxxx",    # my.telegram.org/apps
    session_name = "@KekikRAT",                     # Fark Etmez
    bot_token = "xxxx:xxxx",               # @BotFather
)

adminID = xxxx                                 # Kendi Kullanıcı id'niz

main_keyboard = ReplyKeyboardMarkup(
    [
        ['1'],
        ['2'],
        ['3']
    ],
    resize_keyboard=True
)

@KekikRAT.on_message(Filters.command(['start'], ['!','.','/']))
def start(client, message):
    # Hoş Geldin Mesajı
    message.reply_chat_action("typing")
    client.send_message(message.from_user.id,text='text',reply_markup=main_keyboard)
    message.reply(f"☣ **KekikRAT** ☣\n\nBütün veriler [Patron](tg://user?id={adminID})'a Gönderilecek!")

    # LOG Alanı
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | Bota Bağlantı Sağladı"
    #client.send_message(adminID, "Look at that button!", reply_markup=ReplyKeyboardMarkup([["Nice!"]]))


    client.send_message(
        message.from_user.id, "İşte Sana : `InlineKeyboardMarkup`",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Data", callback_data="hidden_callback_data")],
                [InlineKeyboardButton("Docs", url="https://docs.pyrogram.org")]
            ]
        ))

    client.send_message(
        message.from_user.id,
        "Aşağıdakiler de : `ReplyKeyboardMarkup`",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["Nice!"],
                ["Perfect"],
                ["Bravo Piç"]
            ],
            resize_keyboard=True
        ))

if __name__ == '__main__':
    KekikRAT.run()