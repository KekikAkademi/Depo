from Models_Olustur import taban, KullaniciSinif, BotSinif

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

motor = create_engine('sqlite:///deneme.db')
taban.metadata.bind = motor

db_oturum = sessionmaker(bind=motor)
oturum = db_oturum()

def kullanici_ekle(vatandas:str, tutar:int):
    sorgu = oturum.query(KullaniciSinif).filter(KullaniciSinif.isim==vatandas).first()
    if not sorgu:
        kullanici = KullaniciSinif(isim=vatandas, para=tutar)
        oturum.add(kullanici)
        oturum.commit()

        print("Hallettim")
    else:
        print("Kullanıcı Mevcut")

    oturum.close()

kullanici_ekle('Mehmet', 5)