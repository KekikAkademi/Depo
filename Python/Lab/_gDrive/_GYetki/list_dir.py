# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from json import dumps
GOSTER = lambda bisi : dumps(bisi, indent=2, ensure_ascii=False, sort_keys=False)

from YetkiAlani import g_yetki

def list_dir(drive_id:str=None, folder_id:str=None) -> list:
    """ google drive dizin listeleyici """
    drive_service = g_yetki()

    if drive_id:
        return drive_service.files().list(
            supportsAllDrives           = True,
            supportsTeamDrives          = True,
            includeItemsFromAllDrives   = True,
            corpora     = 'drive',
            teamDriveId = drive_id,
            q           = f"'{folder_id or drive_id}' in parents and trashed=false"
        ).execute()['files']
    else:
        return drive_service.files().list(
                    supportsAllDrives           = True,
                    supportsTeamDrives          = True,
                    includeItemsFromAllDrives   = True,
                    q                           = f"'{folder_id or 'root'}' in parents and trashed=false"
                ).execute()['files']

    #Root Dizini
        # ls /
print(GOSTER(list_dir()))

        # ls /kurek
# print(GOSTER(list_dir(folder_id="1Mdfzz8VXMb55gFCHK2uvlAlOJo415Lox")))              # Kurek


    #Ortak Drive"
        # ls /usr/share/KekikAkademi
# print(GOSTER(list_dir("0ADYmVLSet22XUk9PVA")))                                      # KekikAkademi

        # ls /usr/share/KekikAkademi/Kekik | Eğitim
# print(GOSTER(list_dir("0ADYmVLSet22XUk9PVA", "16BSvNYT5gN7RMMHSYSV1TRDah8jVou2S"))) # Kekik | Eitim