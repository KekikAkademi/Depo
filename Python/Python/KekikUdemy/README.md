# KekikUdemy
Bu araç aşağıdaki adreslerden udemy kuponu çekmek için tasarlanmıştır.
 - https://www.discudemy.com/Turkish/
 - https://www.real.discount/new/

# Kendi Botunu Yap
[BotTaslak.py](https://github.com/KekikAkademi/KekikUdemy/blob/master/Karalamalar/BotTaslak.py "KekikUdemy Bot Taslağı")

    ###############################
    ##KekikUdemy Dökümantasyon#####
    ###############################
    import requests, bs4, lxml, re
    ###############################
    ###################################################
    URL = 'https://www.real.discount/new/'
    SayfaAl = requests.get(URL)
    SayfaOku = bs4.BeautifulSoup(SayfaAl.text, 'lxml')
    ###################################################
    ###############################################
    ##!!!Önce Gelen Linklere bak!!!##
    #################################
    """
    for Link in SayfaOku.find_all('a', href=True):
        print(Link['href'])
    """
    ###############################################
    ##########################################################################
    ##Sonra istediğin filtreyi ayıkla##
    ###################################
    """
    for Link in SayfaOku.find_all(
        'a', attrs={'href': re.compile("^https://www.real.discount/offer/")}
        ):
        
        GelenDiscudemy = Link['href']
        print(GelenDiscudemy)
    """
    ##########################################################################

> Eğer sayfa sayfa taramak istersek;

    ###############################
    ##Döngü İstersen;##
    ###################
    from bs4 import BeautifulSoup
    import requests, bs4, lxml, re
    ###############################
    ##########################################################################################################
    taranacakSayfa = 3
    for SayfaNumarasi in range(1, taranacakSayfa+1):
        URL = 'https://www.real.discount/new/{}'.format(SayfaNumarasi)
        SayfaAl = requests.get(URL)
        SayfaKaynak = SayfaAl.text
        SayfaOku = BeautifulSoup(SayfaKaynak, 'lxml')
        for Link in SayfaOku.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}):
            Linkler = Link['href']
            print(Linkler)
    ##########################################################################################################
    #################################################
            ##Hemen Burda Dönen Linkleri Kaydet######
            #########################################
            print("\tLinkler İşleniyor..")
            LinklerKaydet = open("Linkler.txt", "a")
            LinklerKaydet.write(Linkler + "\n")
            LinklerKaydet.close()
    print("\n\t\tLinkler.txt Kaydedildi..\n")
    ##################################################

> Real.Discount sitesine Udemy linkine ulaşmak için ikinci aşamaya  ihtiyacımız vardır. 
> Bunun için; gelen `Linkler.txt` dosyasını tekrardan taramamız gerekmektedir.

    ##########################################################################################################
    ###İkinci Aşama;###
    ###################################
    from bs4 import BeautifulSoup
    import requests, bs4, lxml, re, os
    ###################################
    Udemy = open("Linkler.txt").readlines() # Udemy bir liste oldu [ ]
    for UdemyVer in Udemy:
    #   print(UdemyVer)  # Udemy'deki listenin her birini for döngüsü ile çıkardık ve yazdırdık
        UdemyURL = UdemyVer
        UdemyURL = UdemyURL.replace("\n","") ## Çekilen Satır Boşluklarını Yok Et
        UdemyResponse = requests.get(UdemyURL)
        UdemyWhole = UdemyResponse.text
        UdemySoup = bs4.BeautifulSoup(UdemyResponse.text, 'lxml')
        for UdemyLinkler in UdemySoup.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}):
            GelenUdemy = UdemyLinkler['href']
            print(GelenUdemy)
    ##########################################################################################################
    ##########################################################################################
            ##Hemen Burda Dönen Linkleri Kaydet######
            #########################################
            print("\tUdemy Linkler İşleniyor..")
            GelenUdemyKaydet = open("Udemylerce.txt", "a") ## Silinecek Eş Gelen Linkler Var!!
            GelenUdemyKaydet.write(GelenUdemy + "\n")
            GelenUdemyKaydet.close()
    print("\n\t\tUdemylerce.txt Kaydedildi..\n")
    os.remove("Linkler.txt")
    print("\n\t\tLinkler.txt Silindi\n") ## Birinci Aşamada Çektiğimiz Gereksiz Linkler
    ##########################################################################################
    ############################################################
    ##Eş Gelen Linkleri Silelim#######################
    ##################################################
    print("\n\t\tÇift Linkler Siliniyor..\n")
    BenzerLink = set() # Bütün Satırları Tut
    SilBenzerLink = open("KekikUdemy.txt", "a")
    for line in open("Udemylerce.txt", "r"):
        if line not in BenzerLink: # Eş çıkmayana kadar döndür
            SilBenzerLink.write(line)
            BenzerLink.add(line)
    SilBenzerLink.close()
    print("\n\t\tÇift Linkler Silindi..\n")
    os.remove("Udemylerce.txt")
    print("\n\t\tUdemylerce.txt Silindi\n") ## Eşli Linkler
    print("\n\t\tKekikUdemy.txt Kaydedildi!!!\n") ## Son Hali
    ############################################################

> Real.Discount sitesine Udemy `a href` bağlantıları birden fazla geçtiği için;
> `Udemylerce.txt` diye bir .txt'ye kaydettik dönen linkleri.
> Ardından `Udemylerce.txt` dosyasındaki eş satırları taratıp, silip `KekikUdemy.txt` dosyasını oluşturduk.


### Bu Bot Hazırlanırken Faydalanılan Kaynaklar;
- https://github.com/raif-py/clickert
- https://youtu.be/Vv_FX3FSvGo
- https://stackoverflow.com/questions/9848889/colorama-for-python-not-returning-colored-print-lines-on-windows
- https://stackoverflow.com/questions/34610162/extract-all-links-from-a-web-page-using-python
- https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
- https://stackoverflow.com/questions/53625255/python-crawling-beautifulsoup-how-to-crawl-several-pages
- https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
- https://stackoverflow.com/questions/26274724/filtering-urls-obtained-using-beautifulsoup

#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..