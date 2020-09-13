import base64
yol = input("Aynı klasordeki resim tam adını yada konum belirterek resmin tam adını giriniz : ")
try:                                                # herhangi bir hata verirse bu eleman ile çökmesini engelleyeceğiz
    with open(yol, "rb") as dosya:                  # Resmimizi read bytes şeklinde açmak zorundayız !
        dosya = base64.encodestring(dosya.read())   # png'imizi okuduk ve base64'e bunu encode etmesini söyledik
        with open(f"{yol}.txt", "wb") as yaz:       # base64 kodumuzu ($yol).txt'e yazacağız . | base64 kodumuz byte halinde !
            yaz.write(dosya)                        # base64 kodumuzu ($yol).txt'e yazdık
            input("Başarılı ile yazıldı !")         # Başarılı olup olmadığı belirtmesi için bir input() verdik
except Exception as hata:
    input("png to base64'e hata ile karşılaşıldı :\n"+hata)  ## Olur da bir hata ile karşılaşırsak ne olduğunu anlamamız gerekiyor