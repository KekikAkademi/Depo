# Python ile Dizi Botu Yapmak

🕊 Bu döküman **[@KekikAkademi](https://t.me/KekikAkademi)** için oluşturulmuştur. ✌🏼

![](https://teletype.in/files/f8/44/f844fcdd-a2eb-4c15-8e46-193ccd80c056.png)

Dostlar merabayın,  
Bu yazımızda `requests` ve `BeautifulSoup` modüllerini kullanarak **dizibox** sitesindeki bütün dizilerin bilgilerini çekmeyi öğreneceğiz.

> **Burada öğrenecekleriniz ile** _istediğiniz websitesinden istediğiniz veriyi rahatlıkla ayıklayabileceksiniz.._

Hadi, hemen başlayalım;

## Senaryo
1.  Siteye **istek**(`request`) **yolla** _ve_ **sana yanıt versin.** 
{`Response [200]`}
2.  Sitedeki **bütün** _dizi_ **linklerini belirle.**
(`Web Crawling`)
3.  **Belirlenen bağlantıları**(_linkleri_) **gez.**
4.  **Gezdiğin linklerden** _dizinin_: _Ad, Açıklama, Ülke ve Tür_ **bilgilerini toparla.**  
    (`Web Scraping`)

### Web Crawling
[Neydi bu olay](https://kekikakademi.site/Python-ile-Veri-Kazima?cda=); _herhangi bir site üzerinde gezinmek ve hedef site üzerinde yer alan linkleri toplamak_ demekti.  
_Web Crawler_’ın temelde yapacağı şey şudur; **belirlenen adresin tüm linklerini taramak ve listelemektir.** _Daha sonra da listelediği bu linklere sırasıyla gider.  
_Bu işlemi otomatize etmek de `Web Crawler` kavramını doğurur.

### Web Scraping
[Neydi bu olay](https://kekikakademi.site/Python-ile-Veri-Kazima?cda=); _Web crawler bir link’e uğradığı zaman_ **devreye Web Scraping kavramı girer.  
Web Scraping**, **link’teki belirtilen alanların toplanması işlemidir.** Yani bir nevi; veri toplama veya yığından veri çıkarma olayıdır.
 `Web Crawler` ve `Web Scraping`_birbirleriyle partner olan kavramlar._

### Kod Zamanı
Öncelikle biz bir robot yazıyoruz değil mi?  
Bakalım ilgili site robotlara ne tavsiye etmiş?

![dizibox.pw/robots.txt](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/3_dizibox_robots_txt.png)

♦ Sitemap'e bakıp kendimize uygun haritayı bulalım ve oraya istek yollayalım.

♦ Ardından bir betik oluşturup kütüphaneleri ekleyerek başlayalım;

    import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
    from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş

♦ Ardından isteğimizi gönderip cevabımıza bakalım;

    link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
    
    istek = requests.get(link)   # link'e istek gönderiyoruz
    
    print(istek)                 # <Response [?]>

![Response](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/1_Response.png)

**Ne oldu?** _403 verdi.._
**Yani?**

![HTTP Status Codes](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/2_HTTP_Status_Codes.png)

**Neymiş _403_ ?**
`Forbidden`  **Erişim Engellendi**

**Neden Peki ?**
İstek yolladığımız site bizi istemiyor olabilir.  
`robots.txt` ne diyordu?

Her türlü `User-Agent` yani **kimlik** kabulüm diyordu.  
_User-Agent tanımlamamız gerekiyor.._

**Deneyelim;**

![User-Agent : @KekikAkademi](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/4_User-Agent_KekikAkademi.png)

**Neymiş?** _Yalan Söylemiş :)_

Şimdi **gerçek** bir kimlik sunalım:  
_iyi hoş da_; **Gerçek Kimliği nasıl bulacağız?**

![User-Agent Bulmak](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/5_User-Agent-Bulmak.png)

1.  Tarayıcımızla gerçek bir kullanıcı olarak websitesine gireceğiz.
2.  Sağ tıklayıp "Sayfayı İncele" veya "Öğeyi Denetle" olan bölümü açacağız.
3.  "Network" sekmesi altındaki "Headers" a geleceğiz.
4.  Kendimiz, şuan hangi kimlik ile istek attığımıza bakacağız.
5.  Bu kimliği kullanarak istek atmayı deneyeceğiz.
######
    #!/usr/bin/env python
    #! -*- coding: utf-8 -*-
    # Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    
    #---------------------------------------------------------------------------------#
    import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
    from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş
    #---------------------------------------------------------------------------------#
    
    link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
    # Gerçek Bir Tarayıcı Olmamız Lazım!
    kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(link, headers=kimlik)       # link'e kimlik bilgimizle istek gönderiyoruz
    
    print(istek)                    # <Response [?]>

![Response 200](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/6_Response_200.png)

**Haarika !**

♦ Artık dönen bir verimiz var ve bunu BeautifulSoup ile işleyeceğiz..

    soup = BeautifulSoup(istek.text, "html5lib")        # Gelen veriyi html5lib ile ayrıştırmaya başlıyoruz
    
    print(soup)

![Gelen Veri (soup)](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/7_Gelen_Veri.png)

**Evveeet!** 
Sonunda tarayıcı üzerinden erişebildiğimiz yere python ile ulaşmayı başardık!  
Sayfanın tamamı elimizde. Şimdi ayıklama zamanı!

**Ekranımızda ne var bize lazım olan?** _Dizi Bağlantıları(Linkleri).._

♦ **Nerede bu linkler?** `<loc>`  _diye bişeyin içinde.._ **Ayıklayalım!**

    print(soup.find('loc'))         # Kaynak Kodundaki <loc>

![<loc>](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/8_loc.png)

**Tuttuk Mu? :)**

`soup.find` diye ayıkladık ya hani; birde bunun `findAll` versiyonu var ;)

    print(soup.findAll('loc'))      # Kaynak Kodundaki <loc>'lar

![findAll('loc)](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/9_findAll_loc.png)

**Ne Oldu?** _Hepsini tablo içinde verdi.._

bu `findAll` olan arkadaşı `for` döngüsü içerisinde kullanırsak; _yinelenebilir bir nesne döndürüyor..._

    for gelenlink in soup.findAll('loc'):
        print(gelenlink)

![for gelenlink in soup.findAll('loc'):](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/10_for_findAll_loc.png)

**Hoppalaaa?** Tamam düzgün verdi ama!!!

Kardeşim dur iki dakika sana aşama aşama öğretiyoruz .  
Geldi mi babacım satır satır düzgünce? Geldi.  
Şimdi kod bloğundan sıyırmak için sadece şunu yapıcaz;

    for gelenlink in soup.findAll('loc'):
        print(gelenlink.text)

![gelenlink.text](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/11_for_findAll_loc_gelenveri_text.png)

**ulan sadece .text ekledin :)** _Atla deve değil, sen asıl olayı seyret şimdi :)_

### Kodları Toparlayalım

    #!/usr/bin/env python
    #! -*- coding: utf-8 -*-
    # Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    
    #---------------------------------------------------------------------------------#
    import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
    from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş
    #---------------------------------------------------------------------------------#
    
    #----------------------------------------------------------------------------------------------------------------------#
    link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
    # Gerçek Bir Tarayıcı Olmamız Lazım!
    kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(link, headers=kimlik)          # link'e kimlik bilgimizle istek gönderiyoruz
    soup = BeautifulSoup(istek.text, "html5lib")        # Gelen veriyi html5lib ile ayrıştırmaya başlıyoruz
    #----------------------------------------------------------------------------------------------------------------------#
    
    #-------------------------------------------------------------#
    #print(istek)                    # <Response [200]>
    #print(soup)                     # Kaynak Kodlar
    #print(soup.find('loc'))         # Kaynak Kodundaki <loc>
    #print(soup.findAll('loc'))      # Kaynak Kodundaki <loc>'lar
    #-------------------------------------------------------------#
    
    for gelenlink in soup.findAll('loc'):
        print(gelenlink.text)

**Senaryomuzun yarısını tamamladık.**

**Neydi?** _Siteden düzgün yanıt al ve bütün dizi linklerini toparla._

Şimdi bu gelen linklere tek tek girme vakti.

    for dizi_adresleri in soup.findAll('loc'):                              # Örümceğimizi Başlattık!
        diziLink = dizi_adresleri.text                                      # Crawl ettiğimiz linkler = Dizi Linkleri
                                                                            # Bu linklerin içine girelim
        dizi_istek = requests.get(dizi_adresleri.text, headers=kimlik)      # Her gelen link'e istek atıyorz
        dizi_icerik = BeautifulSoup(dizi_istek.text, "html5lib")            # html5lib ile parse ediyoruz
        
        print(f"Nerdeyim? : {dizi_adresleri.text}")                         # istek attığımız yeri ekrana yazdır
        print(dizi_icerik)                                                  # Kaynak Kodlar ekrana yazdır
        break                                                               # Döngüyü Kır > Linklerin Hepsini Tarama!

![Scraping Başlangıcı](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/12_scraping_baslangici.png)

**Naptık?**

1.  Örümceği başlat
2.  dizi linklerini toplamıştık zaten
3.  bu linklerin içine gir(istek at)
4.  kaynak kodlarına ulaş
5.  ekrana nerede olduğumuzu yazdır
6.  kaynak kodlarını yazdır
7.  döngüyü kır

1.  döngü içerisinde olduğumuz için
2.  bütün linkleri gezmeden bitmez!

_Geldi Mi?_ **Geldi!**

**Devaaaam!**

Hadi dizi adını alalım, çok basit!

    print(dizi_icerik.title.text)   # Bulunduğumuz Sayfa Başlığını yazdır

![Dizi Başlığı](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/13_dizi_basligi.png)

istediğimiz gibi geldi mi? Hayır.

`.replace("falan","filan")` Özelliğini Kullanalım..

    print(dizi_icerik.title.text.replace(" izle | DiziBOX", ""))

![Dizi Başlığı .replace("","")](https://teletype.in/files/62/51/6251fcdb-da22-47b3-a06b-35d63c5b8e43.png)

**Naptık?** _"izle | DiziBOX"_, olan yeri _""_ hiçbir şey ile değiştirdik ve istediğimiz sonucu elde ettik!

Devam etmeden önce kodlarımızın son haline göz atalım;

![Kodların Son Hali](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/14_kodlarin_son_hali.png)

> Yazı sonunda bu kodların hepsi [github](https://github.com/KekikAkademi) üzerinden paylaşılacak.

Dizi ülkesi ve türünü de çektik mi tamamdır bu senaryo.

**şimdiiiii.....**

Gelen dizi başlığı hangi adresten geliyordu?  
`https://www.dizibox.pw/diziler/100-days-to-victory/`

Bu adrese gidip ayıklamak istediğimiz alanın kaynağına bakalım;

![Dizi Ülkesi](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/15_diziUlkesi.png)

**Nerdeymiş dizi ülkesi bilgimiz?**

`<a` 'nın `rel="tag"` etiketi içerisinde yazı olarak geçiyormuş. Deneyelim bakalım kazımayı..

    diziUlke = dizi_icerik.find("a", attrs={"rel": "tag"}).text
    
    print(diziUlke)

![Dizi Ülkesi Çıktı](https://github.com/KekikAkademi/KekikDiziBotu/raw/master/img/16_diziUlkesi_cikti.png)

`break` ile döngüyü kırdığımız zaman **İngiltere** çıktısını aldık.  
döngüyü kırmayıp devam ettirirsek sırayla diğer sayfaları taramaya devam edip çıktıları verdi.

Ancak şöyle bir sıkıntımız var;

`[https://www.dizibox.pw/diziler/100-days-to-victory/]` adresinde Ülke bilgisinde **İngiltere, Kanada** yazıyor..

Demek ki doğru kazıma yapamamışız. Kodumuzla oynayarak doğru çıktıyı yakalamaya çalışıyoruz..

    diziBilgi = []
    
    for diziData in dizi_icerik.findAll("a", attrs={"rel": "tag"}):     # Bulunduğumuz sayfa içerisinde Dizi Bilgisi
    	diziBilgi.append(diziData.text)
    
    a = ''.join(map(str, diziBilgi[1]))[0]
    
    if a != '2':
    	diziUlkesi = ', '.join(map(str, diziBilgi[:2]))
    	print(diziUlkesi)
    elif a == '1':
    	diziUlkesi = ', '.join(map(str, diziBilgi[:1]))
    	print(diziUlkesi)
    else:
    	diziUlkesi = ', '.join(map(str, diziBilgi[:1]))
    	print(diziUlkesi)

[gibi gibi fantezilere girilebilir](https://github.com/KekikAkademi/KekikDiziBotu/blob/master/KekikDiziBotu.py#L51) tabiki ama konumuzdan çok uzakta :) biz tek ülke ile devam edelim açıkçası bitsin istiyorum artık şu yazı :D

velhasıl bu matematikle beraber her dizinin içine kadar gidebilirsiniz.

ve en son aşamada, örn' 1. sezon 1. bölüm linkinin içerisinde video linki var ;

    https://www.dizibox.pw/freud-1-sezon-1-bolum-izle/5/
    > içerisinde
    
    https://odnoklassniki.ru/videoembed/1795922332305
    > linki var
    
    <a olanları ve href="../odnoklassniki.ru/videoembed/"
    olan linkleri tut;
    
    .findAll('a', attrs={'href':
                  re.compile("^https://odnoklassniki.ru/videoembed/")})

gibi gibi ortalığın anasını bile ağlatabilirsiniz.

Kazıma işi çok sabır gerektiren bir iştir ve ben bu yazı için, aralıklı olarak, 13 saattir uğraşıyorum artık sıkıldım :)

Soru ve Sorunlarınız için [@KekikSiber](https://t.me/KekikSiber) 'den bizlere ulaşabilirsiniz selam ve saygı ile..

### Bu sayfada yazılan; [Kodların Tamamı <<](https://github.com/KekikAkademi/KekikDiziBotu/blob/master/KekikDiziBotu.py)

_Ben bu betikte, dönen veriyi print olarak aldım ama_  
**Siz nasıl isterseniz öyle kullanabilirsiniz. Örn.;**
-   database oluşturun,
-   ister json oluşturun,
-   ister telegram'dan mesaj olarak atın,

_gibi gibi,_ **dönen veriyi nasıl kullanacağınız size kalmış.**

> Görseller [carbon.now.sh](https://carbon.now.sh/?bg=rgba(31%252C129%252C109%252C1)&t=night-owl&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=false&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%2525&si=false&es=2x&wm=false) Sayfası ile Oluşturulmuştur..  

________________________________________________
📃 **Yandex.Disk Bünyemizdeki veriler 1TB'a Ulaşmıştır.. 🎊**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
