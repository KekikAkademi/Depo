# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from apscheduler.schedulers.background import BackgroundScheduler
import time, datetime, os

def arka_plan_zamanlayici():

    def heya():
        print('Heeya! Saat: %s' % datetime.datetime.now())

    zamanlayici = BackgroundScheduler()
    zamanlayici.add_job(heya, 'interval', seconds=3)
    zamanlayici.start()
    print(f"[!] - Çıkmak İçin » Ctrl+{'Break' if os.name == 'nt' else 'C'} «")

    try:
        # Bu, uygulama etkinliğini simüle etmek için buradadır. (ana iş parçacığını canlı tutan)
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Arka plan modu etkinse kesinlikle gerekli değildir, ancak mümkünse yapılmalıdır.
        zamanlayici.shutdown()
        print("\nÇıktım Kanka!")

arka_plan_zamanlayici()