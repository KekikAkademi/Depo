# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from json import dumps
GOSTER = lambda bisi : dumps(bisi, indent=2, ensure_ascii=False, sort_keys=False)

from YetkiAlani import g_yetki

def ortak_drive_listesi() -> list:
    """ google drive ortak drive listeleyici """
    drive_service  = g_yetki()
    ortak_drivelar = drive_service.drives().list(pageSize=10).execute()

    # print(dumps(ortak_drivelar, indent=2, sort_keys=False, ensure_ascii=False))
    # return

    return [
        {"adi": drive["name"], "id": drive["id"]} for drive in ortak_drivelar["drives"]
    ]


print(GOSTER(ortak_drive_listesi()))