"""
fonksiyon içerisine alacağımız parametre sayısını bilmiyorsak '*args' veya '**kwargs' yapılarını kullanırız !
"""
def topla(a, b):
    return a + b
test = topla(5,7)
print(f"'topla' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")
#print(f"'topla' fonksiyonu Sonucu ; {topla(5,7,8)}")       # 2 parametre tanımladık | 3. bir parametre istersek hata döndürür

print() #--------------------------------------------------------------------------------------------------------------#
def toplama(*args):                 # args > argümans | değişken | adı önemli değil : *kurek
    return sum(args)                # sum > toplama fonksiyonu > sum([a,b]) gibi
test = toplama(5,7,8)
print(f"'toplama' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")       # tuple döner : değiştirilemez

def goster(*degerler):
    return degerler
test = goster(5, 7, 'ali')
print(f"'goster' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")

print() #--------------------------------------------------------------------------------------------------------------#
def rehber(**kwargs):               # kwargs değişken | adı önemli değil : *kurek
    return kwargs
test = rehber(isim='ahmet', soyIsim='ali')
print(f"'rehber' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")        # dict. döner

def doviz(**para):
    return para
test = doviz(euro='6.75', dolar='6.34')
print(f"'doviz' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")

print() #--------------------------------------------------------------------------------------------------------------#

"""
args    sonucumuz > tuple(demet) immutable(değiştirilemez) veri tipi olarak döner!
kwargs  sonucumuz > key(anahtar) ve value(değer) olmak üzere dict(sözlük) veri tipi olarak döner!

beraber kullanılacaksa önce args tanımlanmalıdır !! > syntax kuralı!
"""
def beraber(*args, **kwargs):
    return args, kwargs
test = beraber(5, 7, 'ali')
print(f"'beraber' fonksiyonu Sonucu ; {test} | Veri Tipi : {type(test)}")
test2 = beraber(5, 7, 'ali', ad='Mehmet', soyAd='Ali')
print(f"'beraber' fonksiyonu Sonucu ; {test2} | Veri Tipi : {type(test2)}")
print(test2[1])
print(test2[1]['ad'])