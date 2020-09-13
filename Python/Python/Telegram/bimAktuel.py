# TelegramCeo

import asyncio
import logging
import os
import shutil
from collections import Counter

import requests
import wget
from bs4 import BeautifulSoup
from telethon import TelegramClient, errors, events, utils
from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon.tl.custom import Button, MessageButton
from telethon.tl.types import KeyboardButton

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
APP_ID = 'snxnxn'
APP_HASH = 'sjsjdjdj'
BOT_TOKEN = "sjdkdkhdjdj"


bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOT_TOKEN)

markup = bot.build_reply_markup(
    [
        Button.inline('İleri▶️','ileri'),
        # Button.inline('Geri◀️','geri'),
        # Button.inline('Anasayfa⏺','ana'),
        Button.inline('Kapat❌','kapa'),
    ]
)

@bot.on(events.NewMessage(pattern="(/|!).*start ?(.*)"))
async def start(event):
    await bot.send_message(event.chat_id, "BİM Aktüel Ürünleri Almak İçin Bu Botu Kullanabilirsiniz.", buttons=markup, link_preview=False)
    await asyncio.sleep(1)


global j
j=0

tiklayan = []

@bot.on(events.CallbackQuery(pattern='ileri'))
async def callback(event):
    if not os.path.isdir("/workspace/bimaktuel/cop/"):
        os.makedirs("/workspace/bimaktuel/cop/")
    tiklayan.append(event.sender_id)
    c = Counter(tiklayan)
    print(c[event.sender_id])
    sayfa_linki = requests.get('https://www.bim.com.tr/default.aspx', allow_redirects=True)
    soup = BeautifulSoup(sayfa_linki.text, 'html.parser')
    urun = soup.select_one('#form1 > div:nth-child(11) > div.homePage > div.aktuelArea.makeTwo > div > div.productArea > div.row.no-gutters > div > div > div.product.big.col-md-12.col-lg-12.col-xl-9.col-12')
    tarih = soup.find("a",class_="active subButton").text
    if c[event.sender_id]==1:
        urun = soup.select_one('#form1 > div:nth-child(11) > div.homePage > div.aktuelArea.makeTwo > div > div.productArea > div.row.no-gutters > div > div > div.product.big.col-md-12.col-lg-12.col-xl-9.col-12')
    elif c[event.sender_id]:
        print(c[event.sender_id])
        urun = urun.find_next_siblings()[c[event.sender_id]]
    urun_tanim = tarih + "\n\n" + urun.text[:-6]
    link = "https://www.bim.com.tr/"
    resim_link = link + urun.img['src']
    x = wget.download(resim_link,"/workspace/bimaktuel/cop/")
    await event.client.send_file(
        event.chat_id,
        file=x,
        caption=urun_tanim,
        force_document=False,
        buttons=markup
    )
    # shutil.rmtree("/workspace/bimaktuel/cop/")


@bot.on(events.CallbackQuery(pattern='kapa'))
async def kapa(event):
    await start(event)


bot.start()
bot.run_until_disconnected()
