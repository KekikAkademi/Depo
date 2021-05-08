from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

taban = declarative_base()

class KullaniciSinif(taban):
    __tablename__ = 'kullaniciTablo'

    id    = Column(Integer,     primary_key=True, unique=True)
    isim  = Column(String(250), nullable=False,   unique=True)
    para  = Column(Integer,     default=0)


class BotSinif(taban):
    __tablename__ = 'botTablo'

    id    = Column(Integer,      primary_key=True, unique=True)
    isim  = Column(String(250),  nullable=False,   unique=True)
    para  = Column(Integer,      default=0)



# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///deneme.db')

# Tanımladığımız taban üzerindeki tabloları oluşturuyoruz
taban.metadata.create_all(engine)