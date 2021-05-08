from pytube import YouTube
from time import strftime, gmtime
from hurry.filesize import size

yt       = YouTube('https://youtu.be/BqhWfXh_Opg')
videolar = yt.streams.filter(progressive=True)

veri = {
    "bilgi": {
        "sahip"     : yt.author,
        "baslik"    : yt.title,
        "sure"      : strftime("%H:%M:%S", gmtime(yt.length)),
        "tarih"     : yt.publish_date,
        "izlenme"   : yt.views,
        "resim"     : yt.thumbnail_url,
        "aciklama"  : yt.description
    },
    "kaynaklar" : [{
        "kalite" : vid.resolution,
        "boyut"  : size(vid.filesize),
        "url"    : vid.url
    } for vid in videolar]
}

from json import dumps
print(dumps(veri, ensure_ascii=False, sort_keys=False, indent=2, default=str))
