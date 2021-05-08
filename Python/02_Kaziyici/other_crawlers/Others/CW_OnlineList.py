import re
import time
import codecs
import requests
import datetime

# Bugünün Tarihini Alıyoruz
date = datetime.datetime.now().strftime("%d-%m-%Y")

# Üyeler Burda Birikecek
today = []

# Programı Sonsuz Döngüye Sokuyoruz
while True:

    # Online Üyeler Listesini Alıyoruz
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    xml = requests.get("https://www.cyber-warrior.org/Forum/Ajax1433/user.xml", headers = headers).text
    #print(xml)

    # Üyeleri Ayrıştırıp Liste Haline Getiriyoruz
    users = re.findall(r'<Username><!\[CDATA\[(.*?)\]\]></Username>', xml)
    #print(users)

    # Bugün Online Olan Bütün Üyelerin Yanına
    # Şuan Bulduğumuz Üyeleri de Ekliyoruz
    today = today + users
    # print(today)

    # Aynı Üyenin iki kere sayılmasını engelliyoruz
    today = list(dict.fromkeys(today))
    #print(today)

    # Bulduğumuz üyeleri bugünün tarihi ile dosyaya kaydediyoruz.
    file = codecs.open("cw-daily-online-users/{}.txt".format(date), "w+", "utf-8")
    file.write("{} user\n-------------------\n".format(len(today)))
    file.write("\n".join(today))
    file.close()
    print("{}".format(len(today)) + " Kişi Bulundu. \n")
    print(date + " Dosyası Oluşturuldu! \n")

    # Programı 1 dakika uyutuyoruz.
    # Uyutmazsak DDOS yapmış gibi oluruz.
    time.sleep(60)