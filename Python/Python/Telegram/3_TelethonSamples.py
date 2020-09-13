#!/usr/bin/env python
# ! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------------------#
from telethon import TelegramClient, events, sync   #
#---------------------------------------------------#

# / Telegram Bağlantısı -------------------------------------------------#
client = TelegramClient(
    api_id="XXXXXX",                                # my.telegram.org/apps
    api_hash="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",    # my.telegram.org/apps
    session="XXXXXXXXXXXXXXX"                       # Fark Etmez
)
client.start(bot_token="XXXX:XXXXX-XXX")
adminID = "-XXXXXXXXXXXXX"                          # Grup ID
# / Telegram Bağlantısı -------------------------------------------------#

#--------------------------------------------------------------------------------#
@client.on(events.NewMessage(pattern=r'/start'))
async def handler(event):
    await event.reply('Botumuza Hoş Geldin')

    #await client.send_message(adminID, "Heeeya")      # Çalışmıyo!
#--------------------------------------------------------------------------------#

@client.on(events.NewMessage(pattern='(?i).*sea'))
async def handler(event):
    await event.reply('Cami mi lem burası!')

@client.on(events.NewMessage(pattern=r'\.save'))
async def handler(event):
    if event.is_reply:
        yanitlanan = await event.get_reply_message()
        gonderen = yanitlanan.sender
        await client.download_profile_photo(gonderen)
        await event.respond(f'Profil Fotoğrafını Kaydettim @{gonderen.username}!\nGörmek İster Misin?')

client.run_until_disconnected()