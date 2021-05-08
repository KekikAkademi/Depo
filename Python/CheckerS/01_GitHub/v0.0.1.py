import requests
from bs4 import BeautifulSoup


def github(posta, sifre) -> None:
    host    = "github.com"
    origin  = "https://github.com"
    referer = "https://github.com/login"

    headers = {
        "User-Agent"  : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "Host"        : host,
        "Origin"      : origin,
        "Referer"     : referer,
    }

    sess = requests.session()

    payload_icin = BeautifulSoup(sess.get(referer, headers=headers).content, "lxml")

    payload = {
        "commit"             : "Sign in",
        "authenticity_token" : payload_icin.find('input', attrs={"name":"authenticity_token"})['value'],
        "login"              : posta,
        "password"           : sifre,
        "timestamp"          : payload_icin.find('input', attrs={"name":"timestamp"})['value'],
        "timestamp_secret"   : payload_icin.find('input', attrs={"name":"timestamp_secret"})['value']
    }

    print(sess.post('https://github.com/session', headers=headers, data=payload))

    profil = BeautifulSoup(sess.get("https://github.com/settings/profile").content, "lxml")

    adi_soyadi    = profil.find("input", id="user_profile_name")['value']
    kullanici_adi = profil.find("div", class_="f5 text-gray-dark text-bold css-truncate css-truncate-target").text
    e_posta       = profil.find("select", id="user_profile_email").find("option", attrs={'selected' : 'selected'}).text

    print(f"""
    Adı Soyadı    : {adi_soyadi}
    Kullanıcı Adı : @{kullanici_adi}
    e-Posta       : {e_posta}
    Şifre         : {sifre}
    """)

if __name__ == "__main__":
    github(input("E Posta Giriniz : "), input("Sifre Giriniz : "))
