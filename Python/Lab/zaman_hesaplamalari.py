# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

def zaman_donustur(saniye: int) -> str:
    dakika, saniye  = divmod(saniye, 60)
    saat, dakika    = divmod(dakika, 60)
    gun, saat       = divmod(saat, 24)
    toparla = (
        ((str(gun) + " gün, ") if gun else "")
        + ((str(saat) + " saat, ") if saat else "")
        + ((str(dakika) + " dakika, ") if dakika else "")
        + ((str(saniye) + " saniye, ") if saniye else "")
    )
    return toparla[:-2]

tarih       = lambda : datetime.now(timezone("Turkey")).replace(tzinfo=None)
tarih_cevir = lambda tarih : datetime.strptime(tarih, "%d-%m-%Y %X")

ay_atla     = tarih() + relativedelta(months=1)
bi_ay_sonra = ay_atla.strftime("%d-%m-%Y %X")

print(f"""
Tarih       : {tarih()}
Ay Atla     : {ay_atla}

Bugün       : {tarih().strftime("%d-%m-%Y %X")}
Bi Ay Sonra : {bi_ay_sonra}
""")

bugun = tarih()
bitis = tarih_cevir('03-04-2021 01:42:06') # bi_ay_sonra

fark    = bitis - bugun
sn_fark = round(fark.total_seconds())

print(f"Kalan Süre  : {str(zaman_donustur(sn_fark))}")
