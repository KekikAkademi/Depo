tr_harfler = "şçöğüİı"

for harf in tr_harfler:
    if harf == "ö":
        #break                  # döngüyü kır
        continue                # 'ö' yü görmezden gelip devam et 
    print(harf)