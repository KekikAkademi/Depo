# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from konsolTaban import KekikTaban
from os import getcwd as pwd
from time import sleep
from rich.console import Console

taban = KekikTaban(
    baslik   = "@KekikAkademi Betik Tabanı",
    aciklama = "KekikTaban Başlatıldı..",
    banner   = "kekik taban",
    girinti  = 3
)

konsol = Console()

def acilis_sayfasi():
    taban.logo_yazdir('green')
    taban.bilgi_yazdir()

    konsol.print(f"""
    [bold green][[/] [bold yellow]1[/] [bold green]][/] [bold cyan]Bunu Seçersem[/]
    [bold green][[/] [bold yellow]2[/] [bold green]][/] [bold cyan]Şunu Seçersem[/]
    """) # Seçeneklerimizi ayarladık

    konum = pwd()
    if taban.isletim_sistemi == "Windows":
        konum = konum.split("\\")
    else:
        konum = konum.split("/")

    secenek = str(konsol.input(f"[red]{taban.oturum}[/][bright_blue]:~/../{konum[-2] + '/' + konum[-1]}[/] [bold green]>>[/] ")) # Kullanıcı için input oluşturduk

    #-----------------------#
    if secenek == '1':
        taban.logo_yazdir()

        print(1)

        sleep(2)
        acilis_sayfasi()
    #-----------------------#
    elif secenek == '2':
        taban.logo_yazdir()

        print(2)

        sleep(2)
        acilis_sayfasi()
    #-----------------------#
    elif secenek == 'q':
        import sys
        sys.exit()
    #-----------------------#
    else:
        acilis_sayfasi()

if __name__ == '__main__':
    acilis_sayfasi()