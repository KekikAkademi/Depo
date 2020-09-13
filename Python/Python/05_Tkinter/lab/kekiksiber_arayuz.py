#KekikSiber | t.me/kekiksiber | Python ile Sahte Arayüz Oluşturuyoruz
import tkinter                  # arayüz için
import sys                      # dosya ismi|exit için
import time                     # sleep() için
import platform                 # cihaz bilgileri için
from tkinter import messagebox  # tkinter içerisinden messagebox'ı çektik . Böylece hata gösterebileceğiz 

app = tkinter.Tk()          # tkinter penceremizi açtık
image = tkinter.PhotoImage(data="""as4fydhedDh6Iy [dönüştürdüğümüz base64 kodu] qwesTtK35""")
app.title("Lol Money Hack")     # bu kısım gözükmeyecek lakin ginede title ekleyebiliriz
app.iconphoto(1,image)          # ikonumuzu aynı resim olarak belirledik
#app.wm_overrideredirect(True) # Bu kod ile kapat tuşunu ve küçült tuşunun olduğu kısmı komple kaldırıyoruz
#app.attributes("-alpha", 0.9) # Bu kod ile penceremize hafif şeffaflık katıyoruz
# Kodlama aşamasında bu ikisini deaktif etmeniz daha sağlıklı olacaktır


# Uygulamamızı ortalamamız için
windowWidth = app.winfo_reqwidth()     # penceremizin enlemini aldık
windowHeight = app.winfo_reqheight()   # penceremizin boylamını aldık
positionRight = int(app.winfo_screenwidth()/3 - windowWidth/2)  # Pencere konumumuzun enlemini
positionDown = int(app.winfo_screenheight()/3 - windowHeight/2) # Pencere konumumuzun boylamını değiştiriyor.
app.geometry(f"+{positionRight}+{positionDown}")                # Pencere konumumuz ayarlıyoruz

#NOT# positionRight ve positionDown 'da pencereyi ortalarken "3" rakamında değişiklik yapmanız gerekebilir 

app.resizable(0,0)  # Yeniden boyutlandırmayı kapattık
label = tkinter.Label(image=image,text=" ",compound="top",bg="black",fg="white",cursor="watch") 

# image ile label'ımızda resim olacağını belirttik
# text ile penceremizde yazı gösterceğiz . Ama bu'nun değerine neden " " verdik ?
    # Programın açıldıktan sonra biraz bekleyip ardından yazıları göstermesini istiyorum
    # Bunu yaparken pencerede hiç kıpraşma olmaması gerekiyor , bu sebepten " " değerini veriyorz

# compound = "top" ile yazımızı en alta çekiyoruz "center" ile ortalayabilirsiniz
# bg [background olarak da kullanılabilir] "black" değerini vererek arkaplanı tamamen siyah yapıyoruz . "#000" vererek de yapılabilir
# fg [forgorund olarak da kullanılabilir] "white" değerini verek text rengini beyaz yapıyoruz . "#fff" vererek de yapılabilir
# cursor değeri ile label'deki imleci belirliyoruz . "watch" ile yükleniyor imlecini kullanıyoruz

label.pack()    # label'imizi görünür yaptık

app.mainloop()  # penceremizi aktif ettik 