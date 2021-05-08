# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

bot_token = "XXXXXXX"
chat_id   = "555555"

from requests import post

post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}", data={'text': 'Merhaba, Dünya!'})

from telebot import TeleBot

tg_botumuz = TeleBot(bot_token, parse_mode="Markdown")
tg_botumuz.send_message(chat_id, "*Merhaba,* _Dünya!_")