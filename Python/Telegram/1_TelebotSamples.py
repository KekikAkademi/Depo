#!/usr/bin/env python
# ! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-----------------------#
import telebot          #
from time import sleep  #
#-----------------------#

# / Telegram Bağlantısı -------------------------------------------------#
botToken = "XXXX:XXXXX"                                     # Bot Token
adminID = "-XXXXX"                                          # Kanal ID
adminID2 = "-XXXXX"                                         # Grup ID

bot = telebot.TeleBot(botToken)  # telebot'a Tokenimizi bağladık
# / Telegram Bağlantısı -------------------------------------------------#

#--------------------------------------------------------------------------------#
@bot.message_handler(["start"])
def ilk(mesaj):
    # Hoş Geldin Mesajı
    bot.send_chat_action(mesaj.chat.id, 'typing')           # Yazıyor Aksiyonu
    bot.send_message(mesaj.chat.id, "Botumuza Hoş Geldin")  # Mesaj gönder

    # LOG Alanı
    log = f"[{mesaj.from_user.first_name}](tg://user?id={mesaj.from_user.id}) | Bota Bağlantı Sağladı"
    #bot.send_message(adminID, log, parse_mode='Markdown')      # ister kanala
    bot.send_message(adminID2, log, parse_mode='Markdown')     # ister gruba
#--------------------------------------------------------------------------------#

@bot.message_handler(["yardim"])                        # /yardim komutunu aldığında
def yardim(mesaj):
    bot.send_chat_action(mesaj.chat.id, 'typing')       # Yazıyor Aksiyonu
    bot.reply_to(mesaj, "Mesaj Yanıtladım")
    sleep(1)
    sa = bot.send_message(mesaj.chat.id, "Selamın Aleyküm Mükerremin Abi")
    sleep(5)
    bot.edit_message_text("aleyküm selam desene piç", chat_id=mesaj.chat.id, message_id=sa.message_id)

    # Dosya Gönder
    doc = open(r"DocTest_KekikAkademi.txt", 'rb')       # veya "C:\Users\kekik\Desktop\kodlama\DocTest_KekikAkademi.txt"
    bot.send_chat_action(mesaj.chat.id, 'upload_document')      # Dosya Gönderiyor Aksiyonu
    bot.send_document(mesaj.chat.id, doc)

    # Foto Gönder
    foto = open(r"FotoTest_KekikAkademi.png", 'rb')     # veya "C:\Users\kekik\Desktop\kodlama\FotoTest_KekikAkademi.png"
    bot.send_chat_action(mesaj.chat.id, 'upload_photo')         # Fotoğraf Gönderiyor Aksiyonu
    bot.send_photo(mesaj.chat.id, foto)

@bot.message_handler(regexp="kim")                      # cümle içinde eşleşme bulduğunda
def kimsin(mesaj):
    bot.send_chat_action(mesaj.chat.id, 'typing')
    bot.reply_to(mesaj, 'herkesin içişine kimse karışamaz')

bot.polling()