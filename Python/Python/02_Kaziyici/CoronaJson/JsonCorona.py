##############---Kekik---ixakblt---##############
import requests #requests kütphanesini dahil ettik verileri çekebilmek için
url = "https://covid2019-api.herokuapp.com/v2/country/turkey" #verileri aldığımız json datasını url değişkenine atadık
r = requests.get(url) # get isteği atarak veriyi çektik
json_data = r.json() # veriyi json formatına çevirerek json_data nesnesine atadık
ulek = json_data["data"]["location"] #data içerisin de ki location verisini aldık
onay = json_data["data"]["confirmed"] #data içerisin de ki confirmed verisini aldık
olum = json_data["data"]["deaths"] #data içerisin de ki deaths verisini aldık
kurtarilan = json_data["data"]["recovered"] #data içerisin de ki recovered verisini aldık
print("""
            Ülke : {}
            Onaylanan Hasta : {}
            Ölü Sayısı : {} 
            kurtarılan : {}
            """.format(ulek,onay,olum,kurtarilan))  # print ile ekrana bastırdık ve format metodu ile şekillendirdik
