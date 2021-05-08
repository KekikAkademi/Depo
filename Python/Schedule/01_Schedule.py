# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import schedule, os, datetime

class zamanlayici(object):
    def heya(self):
        print('Heeya! Saat: %s' % datetime.datetime.now())

    def baslat(self):
        schedule.every(3).seconds.do(self.heya)

        print(f"[!] - Çıkmak İçin » Ctrl+{'Break' if os.name == 'nt' else 'C'} «")
        while True:
            try:
                schedule.run_pending()
            except KeyboardInterrupt:
                schedule.cancel_job(self.heya)
                print("\nÇıktım Kanka!")
                break


bakalim = zamanlayici()
bakalim.baslat()