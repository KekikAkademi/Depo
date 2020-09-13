# Temel Veri Tipleri
    string      = 'keyiflerolsun'   # Karakter dizisi
    integer     = 1995              # Tam sayı
    float       = 10.07             # Ondalıklı sayı
    boolean     = True veya False   # iki olası değere sahip bir ikili değişken
    list        = []                # liste
    dictionary  = {'key': 'value'}  # sözlük
    tuple       = ()                # değiştirilemez liste

# Matematik Operatörleri
    +   : Toplama
    -   : Çıkarma
    *   : Çarpma
    /   : Bölme
    **  : Üs
    %   : Mod (Bölümden Kalan)
    //  : Tam Bölme (5/2 = 2)

## Çoklu değişken atama ve tek satırda print
    from datetime import datetime

    a, b, c = "Merhaba", "Python!", f"Bugün günlerden;\n\t{datetime.now().strftime('%d-%m-%Y | %H:%M')}"

    print(a, b); print(c)

# İndeks
    yazi[4]         # 4. eleman(index)                  > (4)
    yazi[:5]        # 5. eleman'a kadar                 > (0 1 2 3 4)
    yazi[5:]        # 5. eleman'dan sona kadar          > (5 6 ...)
    yazi[3:6]       # 3. eleman'dan 6. eleman'a kadar   > (3 4 5)
    yazi[2:10:2]    # 2. eleman'dan 6. eleman'a 2'şer   > (2 4 6 8)

# String Metotları(Fonksiyonları)
    yazi.upper()            # bütün harfleri büyüt
    yazi.lower()            # bütün harfleri küçült
    yazi.title()            # kelimelerin ilk harfini büyüt
    yazi.capitalize()       # verinin ilk harfi hariç hepsini küçült
    yazi.center(100)        # 100 karakterli bi konteynır oluştur ve veriyi ortala
    yazi.strip('x')         # x'leri sil (varsayılan paramatre : boşluk)
    yazi.replace(' ','')    # "boşluk" ları "hiçbirşey" e çevir
    yazi.split('x')         # x ile ayrıştırıp listeye çevir (varsayılan parametre : boşluk)
    ' '.join(yazi)          # listeyi string'e çevir arasına boşluk ekle
    yazi.count('a')         # kaç tane 'a' harfi var
    yazi.find('kekik')      # kekik'i ara index'ini ver (mevcut değilse negatif sayı verir)
    yazi.startswith('k')    # 'k' ile mi başlıyor (bool döner {True veya False})
    yazi.endswith('k')      # 'k' ile mi bitiyor (bool döner {True veya False})
    yazi.isalpha()          # değerlerin hepsi alfabetik mi
    yazi.isdigit()          # değerlerin hepsi rakam mı

# Liste Metotları
    liste.append('x')       # listeye x değerini ekle
    liste.insert(3, 'x')    # 3. index'e x değerini ekle
    liste.remove('x')       # x değerini sil
    liste.count('x')        # kaç tane x değeri var
    liste.pop(2)            # 2. değeri sil
    liste.reverse()         # ters çevir
    liste.extend(liste2)    # liste2 listesinin elemanlarını listeye ekle

# Sözlük Metotları
    sozluk.keys()           # anahtarlar
    sozluk.values()         # değerler
    sozluk.items()          # anahtar ve değerler aynı anda döner;
    
        for anahtar, deger in sozluk.items():
            print(f"Anahtar : {anahtar}\tDeğer : {deger}\n")

# jSon Tüyoları
    jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
    jsonCikti = json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
    anahtarlar = [anahtar for anahtar in jsonVeri[0].keys()]