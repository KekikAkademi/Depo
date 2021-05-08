from yetkilendirme import drive_yetkilendirme, yetkilendir

def drive_aramasi(arama_kelimesi, parent_id=None):
    if parent_id:
        sorgu = f"'{parent_id}' in parents and name contains '{arama_kelimesi}'"
    else:
        sorgu = f"name contains '{arama_kelimesi}'"

    drive_service = yetkilendir() or drive_yetkilendirme()
    page_token    = None
    cevap         = ""
    while True:
        try:
            response = drive_service.files().list(
                supportsAllDrives=True,
                q=sorgu,
                spaces="drive",
                fields="nextPageToken, files(id, name, mimeType)",
                pageToken=page_token
                ).execute()
            # print(parent_id)
            # print(response)
            for file in response.get("files", []):
                dosya_adi   = file.get("name")
                dosya_id    = file.get("id")
                if file.get("mimeType") == "application/vnd.google-apps.folder":
                    cevap += f"`[Klasör] {dosya_adi}`\nhttps://drive.google.com/drive/folders/{dosya_id}\n\n"
                else:
                    cevap += f"`{dosya_adi}`\nhttps://drive.google.com/uc?id={dosya_id}&export=download\n\n"
            page_token = response.get("nextPageToken", None)
            if not page_token:
                # daha fazla dosya yoksa
                break

        except Exception as hata:
            cevap += str(hata)
            break
    return f"**Google Drive Araması**:\n`{arama_kelimesi}`\n\n**Sonuçlar**\n\n{cevap}"

print(drive_aramasi('Winrar'))
print(drive_aramasi('PHP', parent_id="0ADYmVLSet22XUk9PVA"))