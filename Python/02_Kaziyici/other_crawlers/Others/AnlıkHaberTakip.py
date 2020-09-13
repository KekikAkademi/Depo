# -*- coding: utf-8 -*-

import time
import mechanize
from bs4 import BeautifulSoup

#mechanize modülü ile tarayıcımızı açtık ve bunu
#br nesnesine atadık.
br = mechanize.Browser()
#Bot olmadığımız belli olasın diye kendimize bir kimlik
#atadık ve robot olarak tarayıcımızı false yaptık.
br.addheaders = [("User-agent","Chrome")]
br.set_handle_robots(False)


id = 78542 #En son haber id degeri buraya kodumuza yapıstırıyoruz.
while True: #İşlemlerimizi sonsuz döngü içinde yapıyoruz.
    #id degerimiz duruma göre degiseceği için linkimize bu şekilde ekledik
    kaynak = br.open("https://bjk.com.tr/tr/mobil/haber?news_id="+str(id)).read()
    #haber kaynağını soup adında bir neseneye atadık ve BeautifulSoup
    # modülünü kullanarak baslık ve icerik çekeceğiz.
    soup = BeautifulSoup(kaynak, "html.parser")
    yaziBaslik = soup.h2 #yazibasliğını böyle çekiyoruz.

    #Eğer bir yazi başlığı boş bir değer ise yani yeni haber paylaşıl-
    #madıysa
    if  yaziBaslik == None:
        print("[-] Yeni bir haber paylasilmamis.")
    #Eğer bir yazi başlığı varsa (bu deger boş değilse) işlemlerimiz bu-
    #rada yapılacak.
    elif yaziBaslik != None:
        print("[+] Yeni bir Haber Bulundu.")
        #Beautful soup ile içerik kısmını HTML olarak çekiyoruz.
        yaziIcerikHTML = soup.find_all("p")
        icerik = ""
        #burada bir liste şeklimde bulunan HTML içeriki tek bir değişke-
        #ne aktarıp (icerik adında), HTML kısımlarını temizliyoruz.
        for i in yaziIcerikHTML:
            icerik = icerik + i.text.encode('utf-8').decode()
        #İçerik ve başlığı birleştirip hepsini bir bütün haline getiriyoruz.
        #upper() ile başlığın bütün harflerini büyük yapıyoruz.
        fullYazi = yaziBaslik.text.encode('utf-8').decode().upper()+"\n"+icerik
        print(fullYazi)
        print("[+] İcerikler Haber Sitesinden Çekildi")
        
        print("""
        Burada islemlerinizi yapabilirsiniz
        ben facebook daki bir sayfamda
        yeni haber eklendikce otonom paylasan bir bot yapmayi dusunuyorum
        """)
        #Yeni yazımızı bulduğumuza göre bundan sonraki yazıya geçmemiz gereki-
        #yor bunun içinde id değerimiz bir arttırıyoruz. Ve bu değere dönüp bak-
        #tığında program yeni bir yazı yoksa olana kadar beklicek ve olunca yine
        #buraya gellip bu değeri arttıracak.
        id = id+1
    
    #Program sürekli değil de 60 saniyelik aralıklarla yeni bir haber paylaşılmış-
    #mı diye baksın
    time.sleep(60)