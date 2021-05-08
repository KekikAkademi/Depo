import requests, sys, time # program içinde kullanılacak modüllerimiz

# program ve raporlamalar için kullanacağımız değişkenleri oluşturuyoruz
sql_inj = list() # hatalar dosyasından okunacak sql hataları bu listeye eklenecek
urller = list() # dosyadan okunacak url'ler bu listeye dahil edilecek
inj_site = list() # sql injection tespit edilen url'ler dosyaya yazılmak için bu listede toplanacak
kontrol = 0 # while döngüsü için kontrol değişkeni
inj_url = 0 # program sonlanırken verilecek istatistik için
hatali_url = 0 # program sonlanırken verilecek istatistik için

try: # herhangi bir hata için
    if sys.argv[3] == "-start": # 4. argüman -start ise programı devam ettiriyoruz
        try: # herhangi bir hata için
            dosya = open(sys.argv[1]) # 2. argüman'a taranacak url'lerin bulunduğu dosyanın adını giriyoruz
            for i in dosya.readlines(): # kaynak dosyamızın satırlarını okuyoruz
                urller.append(i.strip()) # urller listemize ekliyoruz
            hatalar = open("hatalar","r") # url'lerimizde aranacak sql hataları için hatalar dosyasını açıyoruz
            for e in hatalar.readlines(): # hatalar dosyamızdaki satırları okuyoruz
                sql_inj.append(e.strip()) # sql_inj listemize ekliyoruz
        except: # hatalı veya eksik dosyalar için bu hatayı yazdırıyoruz
            mesaj = "\n{} veya hatalar eksik."
            print(mesaj.format(sys.argv[1]))
            quit()
        print("")
        print(len(urller), "URL taranacak.\n")
        print("Tarama başladı...", time.strftime('%X'), "\n")
        while kontrol < len(urller): # while döngümüz taranacak url sayımız kadar devam edecek
            for url in urller: # urller listemizi for döngüsüne sokup tek tek işleme alıyoruz
                tampon = url.replace("=", "='") # url'i sql hatası vermeye zorlamak için url'de bulunan = işaretini =' olarak replace ediyoruz ve tampon değişkenimize atıyoruz
                try: # hatalar için
                    urlKaynak = requests.get(tampon) # requests.get ile replace edilen url'e bağlanıyoruz ve urlKaynak değişkenimize atıyoruz
                    texteCevir = urlKaynak.text # çekilen tüm içeriği text'e çeviriyoruz
                    if urlKaynak.status_code == 200: # eğer bağlandığımızda dönen http kodu 200 ise
                        for hata in sql_inj: # sql_inj listemizde bulunan hataları tek tek işleme sokuyoruz
                            if hata in texteCevir: # eğer hatamız texte çevirdiğimiz içeriğin içinde varsa
                                print("SQLi:", url, "\n")
                                kontrol += 1 # while döngüsünü kontol etmek için kontrol değişkenimizi 1 artırıyoruz
                                inj_url += 1 # istatistik için injectable url sayısını 1 artırıyoruz
                                inj_site.append(url) # dosyaya yazılmak üzere inj_site listemize ekliyoruz
                            else: # eğer hatamız texte çevirdiğimiz içeriğin içinde yoksa
                                kontrol += 1 # while döngüsünü kontol etmek için kontrol değişkenimizi 1 artırıyoruz
                    elif urlKaynak.status_code == 500: # eğer bağlandığımızda dönen http kodu 500 ise
                        print("Blind SQL var!") # yaz
                        inj_site.append(url+" Blind") # sonuna "Blind" notu ekleyip dosyaya yazılmak üzere inj_site listemize ekliyoruz
                        kontrol += 1 # while döngüsünü kontol etmek için kontrol değişkenimizi 1 artırıyoruz
                except: # yanlış url'lerden ötürü hata alırsak
                    print("Hatalı URL. Ulaşılamadı.\n") # yaz
                    kontrol += 1 # while döngüsünü kontol etmek için kontrol değişkenimizi 1 artırıyoruz
                    hatali_url += 1 # istatistik için hatali url sayısını 1 artırıyoruz
                    continue # hata alsan bile döngüye devam et
        print("\nTarama bitti.", time.strftime('%X'), "\n")
        print("{} / {} URL'de SQL Injection bulundu. {} URL hata verdi ve taranamadı." .format(len(urller), inj_url, hatali_url))
        sdosya = open(sys.argv[2], "w")
        sdosya.writelines(inj_site)
        sdosya.close()
        print("\n"+sys.argv[2], "dosyasına kaydedildi.")
    else:
        print("Parametre Hatalı")
except:
    print('''
 -------------------------------------------------------------
|                                                             |
|       Multi Error Based & Blind SQL Injection Checker       |
|                                                             |
|                            NDorte                           |
|                                                             |    
|  Usage: python sqlichecker.py source_list save_list -start  |
|                                                             |
 -------------------------------------------------------------
    ''')
