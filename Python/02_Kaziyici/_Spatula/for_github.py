# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from tabulate import tabulate

from w_bs4.coinMarketCap import coinMarket
from w_bs4.nobetciEczane import nobetciEczane
from w_bs4.haberler import sonDakika
from w_bs4.havaDurumu import hava_Durum
from w_bs4.bim import aktuelBim
from w_bs4.akaryakit import akaryakitFiyat

from w_pandas.doviz import dovizVerileri
from w_pandas.deprem import depremVerileri

def md_github(veri):
    """
    Verilen veriyi github md tablo diline çevirir...
    """

    return tabulate(veri, headers='keys', tablefmt='github')

# with open("coinMarket.md", "w+") as coin:
#     coin.write(md_github(coinMarket('json_veri')))

# try:
#     with open("nobetciEczane.md", "w+") as nobetci:    
#         nobetci.write(md_github(nobetciEczane('çanakkale', 'merkez', 'json_veri')))
# except:pass

# with open("dovizVerileri.md", "w+") as doviz:
#     doviz.write(md_github(dovizVerileri('json_veri')))

# with open("havaDurumu.md", "w+") as hava:
#     hava.write(md_github(hava_Durum("Çanakkale", "Merkez", "json_veri")))

# with open("haberler.md", "w+") as haber:
#     haber.write(md_github(sonDakika("json_veri")))

# with open("deprem.md", "w+") as deprem:
#     deprem.write(md_github(depremVerileri("json_veri")))

# with open("bim.md", "w+") as bim:
#     bim.write(md_github(aktuelBim("json_veri")['urunler']))

with open("akaryakit.md", "w+") as akaryakit:
    akaryakit.write(md_github(akaryakitFiyat("json_veri")))