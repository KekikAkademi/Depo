# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from yetkilendirme import drive_yetkilendirme, yetkilendir

def ortak_drive_listesi():
    """ telegram için ortak drive listesi çıkartır """
    drive_service = yetkilendir() or drive_yetkilendirme()
    ortak_drivelar = drive_service.drives().list(pageSize=10).execute()

    import json
    print(json.dumps(ortak_drivelar, indent=2, sort_keys=False, ensure_ascii=False))
    return

print(ortak_drive_listesi())