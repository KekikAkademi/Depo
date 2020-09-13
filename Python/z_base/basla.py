# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from kekikTaban._renkler import *
from kekikTaban._evrensel import *
from kekikTaban._degiskenler import *

from fonksiyonlar import bakalim, dongu
from time import sleep

#-----------------------------------#
def acilisSayfasi():
    print(yesil + logo)     # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)        # Üst Bilgimizi yazdırdık
    print(f"""
    {yesil}[{sari} 1 {yesil}] {cyan}Bunu Seçersem
    {yesil}[{sari} 2 {yesil}] {cyan}Şunu Seçersem
    """) # Seçeneklerimizi ayarladık

    konum = os.getcwd()
    if isletim_sistemi == "Windows":
        konum = konum.split("\\")
    else:
        konum = konum.split("/")

    secenek = str(input(f"{kirmizi}{oturum}:{l_mavi}~/../{konum[-2] + '/' + konum[-1]} >> {yesil}")) # Kullanıcı için input oluşturduk

    #-----------------------#
    if secenek == '1':
        temizle()
        print(l_mavi + logo)
        print(ust_bilgi)


        bakalim.kurek()
        sleep(2)
        acilisSayfasi()
    #-----------------------#
    elif secenek == '2':
        temizle()
        print(l_mavi + logo)
        print(ust_bilgi)


        dongu.kisir()
        sleep(2)
        acilisSayfasi()
    #-----------------------#
    elif secenek == 'q':
        import sys
        sys.exit()
    #-----------------------#
    else:
        temizle()
        acilisSayfasi()


if __name__ == '__main__':
    acilisSayfasi()