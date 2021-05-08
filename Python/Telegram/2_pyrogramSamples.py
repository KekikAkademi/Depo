#!/usr/bin/env python
# ! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------# 
from pyrogram import Client, filters    #
from time import sleep                  #
#---------------------------------------#

# / Telegram Bağlantısı -------------------------------------------------#
app = Client(
    api_id=XXXXXXXX,                                # my.telegram.org/apps
    api_hash="XXXXXXXX",                            # my.telegram.org/apps
    session_name = "XXXXXXXXX",                     # Fark Etmez
    bot_token = "XXXXXXX:XXXXXXXX"                  # @BotFather
)

adminID = -XXXXXXXXXXX                              # Grup ID
# / Telegram Bağlantısı -------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#
@app.on_message(filters.command(['start'], ['!','.','/']))
async def ilk(client, message):
    # Hoş Geldin Mesajı
    await message.reply_chat_action("typing")             # https://docs.pyrogram.org/api/bound-methods/Message.reply_chat_action
    await message.reply("Botumuza Hoş Geldin")

    # LOG Alanı
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | Bota Bağlantı Sağladı"
    await client.send_message(adminID, log)
#----------------------------------------------------------------------------------------------------------------------#

@app.on_message(filters.command(['yardim'], ['!','.','/']))     # ! . / yardim komutunu aldığımda
async def komutDeneme(client, message):
    await message.reply_chat_action("typing")                         # Yazıyor Gönderiyor Aksiyonu
    await message.reply_text("Komut Aldım!", quote=True)  # https://docs.pyrogram.org/api/bound-methods/Message.reply_text
    sleep(1)
    sa = await message.reply_text("Selamın Aleyküm Mükerremin Abi")
    sleep(5)
    await sa.edit("aleyküm selam desene piç")

    # Dosya Gönder
    await message.reply_chat_action("upload_document")                # Fotoğraf Gönderiyor Aksiyonu
    dosya = "DocTest_KekikAkademi.txt"
    await message.reply_document(dosya)

    # Foto Gönder
    await message.reply_chat_action("upload_photo")                   # Dosya Gönderiyor Aksiyonu
    foto = "FotoTest_KekikAkademi.png"
    await message.reply_photo(foto)

@app.on_message(filters.regex('kim'))                           # cümle içinde eşleşme bulduğunda
async def kimsin(client, message):
    await message.reply_chat_action("typing")
    await message.reply_text("herkesin içişine kimse karışamaz")

if __name__ == "__main__":
    app.run()
