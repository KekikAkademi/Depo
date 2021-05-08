def ytdlProgress(data: dict):
    if data['status'] == "downloading":
        simdi = time()
        tahmini_toplam_sure = data.get('eta')
        hiz = data.get('speed')
        if not (tahmini_toplam_sure and hiz):
            return
        
        gecerli = data.get('downloaded_bytes')
        toplam = data.get("total_bytes")
        if gecerli and toplam:
            yuzde = int(gecerli) * 100 / int(toplam)
        
        cikti = "**[{}{}]**\n**Süreç**: `%{}`\n".format(
            ''.join(('█' for _ in range(floor(yuzde / 5)))),       # █●
            ''.join(('░' for _ in range(20 - floor(yuzde / 5)))),  # ░○
            int(yuzde)
        )

        cikti += f'**Dosya Adı :** `{data["filename"]}`\n'
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

import youtube_dl
from time import time
from math import floor

class LogYok(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

def ytDLSiki(link, cikti=None):
    """ Verilen Youtube Linkini İndirir.."""
    parametreler = {
        'outtmpl' : '%(title)s.%(ext)s',
        'cachedir': False,
        'logger' : LogYok(),
        'progress_hooks': [ytdlProgress],
    }

    if cikti == 'mp3':
        parametreler.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        parametreler.update({
            'format': 'best',
        })

    ytdl = youtube_dl.YoutubeDL(parametreler)

    ytdl.download([link])

# ytDLSiki('http://www.youtube.com/watch?v=kCsq4GAZODc')
# ytDLSiki('http://www.youtube.com/watch?v=kCsq4GAZODc', 'mp3')


#----------------------------------------------------------------#

class SimpleYDL(youtube_dl.YoutubeDL):
    def __init__(self, *args, **kargs):
        super(SimpleYDL, self).__init__(*args, **kargs)
        self.add_default_info_extractors()


def get_videos(url, extra_params={}):
    '''
    Get a list with a dict for every video founded
    '''
    ydl_params = {
        'format': 'best',
        'cachedir': False,
    }

    ydl_params.update(extra_params)
    ydl = SimpleYDL(ydl_params)
    
    return ydl.extract_info(url, download=False)

import json

# print(json.dumps(get_videos("http://www.youtube.com/watch?v=396gGW4VhM4"), indent=2, sort_keys=False, ensure_ascii=False))
# qsort = get_videos('http://www.youtube.com/watch?v=396gGW4VhM4')
# print(qsort.get('title'))