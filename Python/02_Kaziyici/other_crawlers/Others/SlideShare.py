# -*- coding: utf-8 -*-

import urllib.request
from fpdf import FPDF
from bs4 import BeautifulSoup

#Bu kısımda mevcut slayta ait source kodları çekiyoruz.
url=input("Lütfen İndirmek istediğiniz slayt dosyasının bulunduğu web urlsini yazın:")
response=urllib.request.urlopen(url)
data=response.read()
response.close()
liste=[]
#elde ettiğimiz dosyayı aşağıda parse ediyoruz ve gerekli olan kısımları Liste adındaki listede tutuyoruz.
soup=BeautifulSoup(data,"html.parser")
for i in soup.find_all("img",attrs={"class":"slide_image"}):
    liste.append(i["data-full"])
sayaç=0

#benim yaptığım örnek 300 sayfalı bir slayt idi onda hatasız bir şekilde ilerledi.
#liste tam istediğim şekilde oluştu o yüzden ekstra işlem yapmama gerek kalmadı 300 sayısınıda listenin len özelliğini kullanrak aldım
#indirdiğim resimleri mevcut dizine kayıt ettirdim.
for i in liste:
    sayaç=sayaç+1
    image=urllib.request.urlopen(i)
    byte=image.read()
    image.close()
    f=open(str(sayaç)+".jpg","wb")
    f.write(byte)
    f.close()
    print(sayaç,"nolu sayfa bitti.")
    

#burasıda pdf haline getirdiğim kısım zaten basit
sayaç=0
imagelist=[]
pdf = FPDF()
while sayaç<int(len(liste)):
    sayaç=sayaç+1
    imagelist.append(str(sayaç)+".jpg")

print("Bir kısım İşlem tamamlandı.")

for image in imagelist:
    pdf.add_page("P")
    pdf.image(image,10,10,190,278)#şu kısımda rakamlar tamamen deneme yanılmayla buldum görsele göre ayarlamak lazım.
    print(image," bitti")

print("PDF Çıktısı oluşturuluyor Lütfen bekleyin.")

pdf.output("YeniPDF.pdf", "F")

print("bitti")
