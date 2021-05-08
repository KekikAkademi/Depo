# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from yetkilendirme import drive_yetkilendirme
from googleapiclient.http import MediaFileUpload
from mimetypes import guess_type
import os, json, math

bilgiler = json.load(open("bilgiler.json"))

async def tg_drive(dosya_yolu, mesaj, ortak_drive_isim=None):
    """ google drive a dosya yükler ve progress verir """
    drive_service = drive_yetkilendirme()

    mime_turu = guess_type(dosya_yolu)[0]
    mime_turu = mime_turu or "text/plain"
    dosya_adi = os.path.basename(dosya_yolu)

    nerdeyiz = None
    if ortak_drive_isim:
        ortak_drivelar = drive_service.drives().list(pageSize=10).execute()
        for ortak_drive in ortak_drivelar['drives']:
            if ortak_drive['name'] == ortak_drive_isim:       # Ortak Drive ADI
                ortak_drive_id = ortak_drive['id']
                nerdeyiz = ortak_drive['name']
            else:
                continue

        govde = {
            "name": dosya_adi,
            "description": f"{bilgiler['session']} üzerinden yüklenmiştir..",
            "mimeType": mime_turu,
            "parents": [ortak_drive_id]
        }
    else:
        govde = {
            "name": dosya_adi,
            "description": f"{bilgiler['session']} üzerinden yüklenmiştir..",
            "mimeType": mime_turu
        }

    dosya_govde = MediaFileUpload(dosya_yolu, mimetype=mime_turu, chunksize=50*1024*1024, resumable=True)
    yuklenen_dosya = drive_service.files().create(body=govde, media_body=dosya_govde, supportsAllDrives=True).execute()

    yanit = None
    gorunen_mesaj = ""
    while yanit is None:
        durum, yanit = yuklenen_dosya.next_chunk(num_retries=5)
        if durum:
            yuzde = int(durum.progress() * 100)
            progress_str = "**[{0}{1}]**\n**Süreç** : __%__`{2}`\n".format(
                "".join(["●" for _ in range(math.floor(yuzde / 5))]),
                "".join(["○" for _ in range(20 - math.floor(yuzde / 5))]),
                round(yuzde, 2),
            )
            gecerli_mesaj = f"**Arşive yüklüyorum kanka..**\n**Dosya Adı**: `{dosya_adi}`\n{progress_str}"
            if gorunen_mesaj != gecerli_mesaj:
                await mesaj.edit(gecerli_mesaj)
                gorunen_mesaj = gecerli_mesaj

    dosya_id = yanit.get("id")

    mesaj = ""
    mesaj += f"`{nerdeyiz}` **Dizinine** " if nerdeyiz else "`Root` **Dizinine** "
    mesaj += f"__Yükledim Kanka.. :__"
    link = f"https://drive.google.com/open?id={dosya_id}"

    return mesaj, link, dosya_adi