def pafyProgress(toplam, gecerli, ratio, hiz, tahmini_toplam_sure):
    simdi = time()
    if not (tahmini_toplam_sure and hiz):
        return
    if gecerli and toplam:
        yuzde = int(gecerli) * 100 / int(toplam)
    
    cikti = "**[{}{}]**\n**Süreç**: `%{}`\n".format(
        ''.join(('█' for _ in range(floor(yuzde / 5)))),       # █●
        ''.join(('░' for _ in range(20 - floor(yuzde / 5)))),  # ░○
        int(yuzde)
    )

    # cikti += f'**Dosya Adı :** `{baslik}`\n'
    cikti += f"**Başarılı:** `{okunabilirByte(toplam)}`__'dan__ **{okunabilirByte(gecerli)}**\n"
    cikti += f"**Hız:** `{okunabilirByte(hiz)}/s`\n"
    cikti += f"**Tahmini:** __{zamanDonustur(tahmini_toplam_sure)}__\n"
    
    print(cikti)

def okunabilirByte(boyut: int) -> str:
    """ baytları okunabilir biçime dönüştürür """
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not boyut:
        return ""
    binyirmidort = 2 ** 10
    say = 0
    cikti_sozluk = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while boyut > binyirmidort:
        boyut /= binyirmidort
        say += 1
    return str(round(boyut, 2)) + " " + cikti_sozluk[say] + "B"

def zamanDonustur(saniye: int) -> str:
    """ Saniyeleri okunabilir biçime dönüştürür """
    dakika, saniye = divmod(saniye, 60)
    saat, dakika = divmod(dakika, 60)
    gun, saat = divmod(saat, 24)
    toparla = (
        ((str(gun) + " gün, ") if gun else "")
        + ((str(saat) + " saat, ") if saat else "")
        + ((str(dakika) + " dakika, ") if dakika else "")
        + ((str(saniye) + " saniye, ") if saniye else "")
    )
    return toparla[:-2]


from time import time
from math import floor
import pafy

# url = "http://www.youtube.com/watch?v=kCsq4GAZODc"
# paf_kuf = pafy.new(url)

# vid = paf_kuf.getbest()
# baslik = paf_kuf.title
# vid_dosyasi = vid.download(quiet=True, callback=pafyProgress)

# ses = paf_kuf.getbestaudio()
# baslik = paf_kuf.title
# ses_dosyasi = ses.download(quiet=True, callback=pafyProgress)

# list_test = pafy.get_playlist('https://www.youtube.com/playlist?list=PL59FEE129ADFF2B12')
# for vid in list_test['items']:
#     liste_vid = vid['pafy'].getbest()
#     baslik = vid['pafy'].title
#     liste_dosyasi = liste_vid.download(quiet=True, callback=pafyProgress)