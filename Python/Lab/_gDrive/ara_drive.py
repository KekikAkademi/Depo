# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot.Edevat._drive.yetkilendirme import g_yetki

drive_service  = g_yetki()

def ara_drive(drive_id:str, dizin_id:str, mim_turu:str=None, arama_kelimesi:str=None) -> str:
    # https://developers.google.com/drive/api/v3/search-files

    if mim_turu:
        sorgu = f"mimeType = '{mim_turu}' and '{dizin_id}' in parents"
    elif arama_kelimesi:
        sorgu = f"'{dizin_id}' in parents and name contains '{arama_kelimesi}'"
    else:
        sorgu = f"'{dizin_id}' in parents"

    sonraki_sayfa = None
    cevap         = ""
    while True:
        # https://developers.google.com/drive/api/v3/enable-shareddrives
        yanit = drive_service.files().list(
            supportsAllDrives           = True,
            supportsTeamDrives          = True,
            includeItemsFromAllDrives   = True,
            corpora                     = 'drive',
            teamDriveId     = drive_id,
            q               = sorgu
        ).execute()
        # print(yanit)

        for dosya in yanit.get("files", []):
            dosya_adi   = dosya.get("name")
            dosya_id    = dosya.get("id")

            if dosya.get("mimeType") == "application/vnd.google-apps.folder":
                cevap += f"📁 {dosya_adi}\n🔗 https://drive.google.com/drive/folders/{dosya_id}\n\n"
            else:
                cevap += f"📄 {dosya_adi}\n🔗 https://drive.google.com/uc?id={dosya_id}&export=download\n\n"

        sonraki_sayfa = yanit.get("nextPageToken", None)
        if not sonraki_sayfa:
            # daha fazla dosya yoksa
            break

    return cevap

# print(ara_drive(drive_id='0ADYmVLSet22XUk9PVA', dizin_id='1BUZgJDqXY0Hi2wNcjKl-TMO5Nufz4M8r'))
# print(ara_drive(drive_id='0ADYmVLSet22XUk9PVA', dizin_id='1BUZgJDqXY0Hi2wNcjKl-TMO5Nufz4M8r', arama_kelimesi='Java'))
