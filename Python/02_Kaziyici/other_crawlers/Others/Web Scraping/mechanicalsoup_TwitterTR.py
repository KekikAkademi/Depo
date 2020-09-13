## https://www.turkhackteam.org/python/1861640-mechanicalsoup-python-checker-yapimi-umutkalay.html

import mechanicalsoup

useragent_bilgisi = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
referer_bilgisi = "https://twitter.com/"

br = mechanicalsoup.StatefulBrowser() # Tarayıcı nesnesi oluşturduk
#br.session.proxies = {"http":"http://1.1.1.1:8080","https":"https://1.1.1.1:8080"} # Proxy ayarlarını değiştirdik
#br.session.proxies.update({"http":"http://1.1.1.1:8080","https":"https://1.1.1.1:8080"}) # Bir üst deki koddan farkı sahte proxy olmasıdır. Siteye bu proxy üzerinden bağlandığını beyan ederken aslında gerçek ip üzerinden işlem yapar proxy çalışmasa bile sıkıntı olmaz twitter gibi bir çok site de bunu afiyetle yer!
br.session.headers = {"User-Agent":useragent_bilgisi,"referer":referer_bilgisi } # User-Agent ve referer ayarlarını değiştirdik.
br.session.headers.update({"User-Agent":useragent_bilgisi,"referer":referer_bilgisi }) # Proxy deki update gibi sahte bilgi beyan eder.


Baglanti = br.open("https://twitter.com/login") # Ve bir siteye bağlantı isteği gönderdik
BulundugumuzYer = br.get_url() #Şu anda işlemin bulunduğu sayfa link ini döndürür
SayfaVerileri = br.get_current_page() #Site verilerini içe çekmek için kullanılır
"""
BeautifulSoup import etmeksizin BeautifullSoup içerisindeki modülleri kullanmamız mümkün.
br.get_current_page().find_all()
gibi
"""
FormBilgileri = br.get_current_page().find_all('form') #Sayfa içindeki form bilgilerini döndürür

print(Baglanti) # <Response [200]> #Başarı durumunda response 200 şeklinde bir dönüt döndürür
print(BulundugumuzYer) # https://twitter.com/login
#print(SayfaVerileri)
print(FormBilgileri)

"""
br.select_form('form[action="https://twitter.com/sessions"]') # Sayfa içerisinde doldurmak istediğimiz formun action değerini yazdık ve seçtik.Sonraki adımlar bu form üzerinden devam edecek
br.get_current_form().print_summary() # Seçtiğimiz form içerisindeki kodu döndürür
br["session[username_or_email"] = "Kullanıcı adı" #Form içerisindeki kullanıcı adı kısmını seçtik ve yazmak istediğimiz kullanıcı adını yazdık
br["session[password]"] = "Parola" #Kullanıcı parolamızı yazdık
br.submit_selected() # Ve giriş butonuna tıkladık. 1 den fazla buton varsa formun içerisinde parantez içerisine buton bilgileri eklenmeli.
br.launch_browser() #Modülün bir sayfa açmadan işlem gerçekleştirdiğini söylemiştik fakat yinede sayfa içi yaptığımız işlemleri görmek istersek bu fonksiyonu kullanabiliriz. Unutmayalım ki gerçek bir sayfa açılmayacak.

"""