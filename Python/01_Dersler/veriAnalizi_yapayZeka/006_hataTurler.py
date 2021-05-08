"""
Yazılımcı Hataları;

prit("deneme"
    SyntaxError             > syntax

print(5/0)
    ZeroDivisionError       > Bir Sayı sıfıra bölünemez

print(degisken)
    NameError               > Tanımlanmayan değer

int('String ifade')
    ValueError              > Uyumsuz veri
"""

"""
Program Hatası veya Mantık Hatası(BUG);

uzunKenar = 5
kisaKenar = 2
alan = 2 * uzunKenar * kisaKenar
print(alan)
    Hata dönmez fakat sonuç yanlış !

Kullanıcının karşılaşabileceği hataları input'da bölünen yerine harf girerse hatasını gidermemiz lazım!
    try - except
"""