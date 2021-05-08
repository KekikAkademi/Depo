# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import os, datetime

async def heya():
    print('Heeya! Saat: %s' % datetime.datetime.now())


if __name__ == '__main__':
    zamanlayici = AsyncIOScheduler()
    zamanlayici.add_job(heya, 'interval', seconds=3)
    zamanlayici.start()
    print(f"[!] - Çıkmak İçin » Ctrl+{'Break' if os.name == 'nt' else 'C'} «")

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        print("\nÇıktım Kanka!")