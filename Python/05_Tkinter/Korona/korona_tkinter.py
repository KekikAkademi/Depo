# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

from time import sleep, strftime
from kaziyici.json_korona import yazilan_veri

pencere = tkinter.Tk()
resim = Image.open("korona.png")
arkaplan_image = ImageTk.PhotoImage(resim)

pencere.geometry('790x470')
#pencere.attributes('-fullscreen', True)    #Tam ekran moduna gecis.
pencere.configure(bg='black')
pencere.title("Corona Virus Sayaacı - @KekikAkademi")
pencere.wm_overrideredirect(True)   # Başlık-Kapat-Küçült Tuşlarının olduğu kısmı kaldırıyoruz
pencere.attributes("-alpha", 0.9)   # Penceremize hafif şeffaflık katıyoruz
pencere.resizable(0, 0)             # Yeniden boyutlandırmayı kapattık

positionRight = int(pencere.winfo_screenwidth() / 3 - pencere.winfo_reqwidth() / 2)    # Pencere konumumuzun enlemini değiştiriyoruz
positionDown = int(pencere.winfo_screenheight() / 3 - pencere.winfo_reqheight() / 2)   # Pencere konumumuzun boylamını değiştiriyoruz
pencere.geometry(f"+{positionRight}+{positionDown}")                        # Pencere konumumuz ayarlıyoruz
    # NOT # positionRight ve positionDown 'da pencereyi ortalarken "2.5" rakamında değişiklik yapmanız gerekebilir

def acilCikis():
    print ("Sağlıklı Günler")
    pencere.destroy()
    sys.exit(0)

while True:
    cerceve = Canvas(pencere, width=810, height=490, background="black")
    cerceve.create_image(400, 240,  image=arkaplan_image)
    cerceve.place(x=-3,y=-3)
    
    cikisButonu = Button(pencere, text=f"Pencereyi Kapat", command = acilCikis)
    cikisButonu.pack(side=BOTTOM)
    
    for bilgi in yazilan_veri['koronaVerileri']:
        vakaSayisi = Label(pencere, text=(bilgi['vakaSayisi']['dunyaGeneli']), bg="white", fg="black", font="Helvetica 25 bold")
        vakaSayisi.place(x=430, y=185)

        oluSayisi = Label(pencere, text=(bilgi['oluSayisi']['dunyaGeneli']), bg="white", fg="black", font="Helvetica 18 bold")
        oluSayisi.place(x=370, y=345)

        iyilesmeSayisi = Label(pencere, text=(bilgi['iyilesmeSayisi']['dunyaGeneli']), bg="white", fg="black", font="Helvetica 18 bold")
        iyilesmeSayisi.place(x=615, y=345)

    #pencere.update()
    pencere.mainloop()
    sleep(5)