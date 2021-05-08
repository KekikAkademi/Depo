import eel
from KekikSpatula import NobetciEczane

eel.init('www')

@eel.expose
def py_eczane(il, ilce):
    mesaj = f"Aranan Nöbetçi Eczane : {ilce} / {il}\n"
    eczaneler = NobetciEczane(il, ilce).veri['veri']
    for eczane in eczaneler:
        mesaj += f"\n⚕ {eczane['ad']}"
        mesaj += "\n📍"
        if eczane['mahalle']:
            mesaj += f"`{eczane['mahalle']}`\n"
        mesaj += f"{eczane['adres']}"
        if eczane['tarif']:
            mesaj += f"\n({eczane['tarif']})"
        mesaj += f"\n☎️ {eczane['telefon']}\n\n"

    print(mesaj)
    eel.eczaneVer(mesaj.replace("\n","<br />\n"))

eel.start('index.html')