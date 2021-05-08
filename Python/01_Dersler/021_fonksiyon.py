def kimO(isim="kilimci", soyisim=""):                               # varsayılanı olmayan(zorunlu olan) değer sonda olamaz
    print(f"TIK TIK TIK KİM O?\n\t{isim} {soyisim} Geldi Hanım !")

kimO()
kimO("ali")
kimO("mehmet", "ali")

def kimO2(isim, soyisim="kilimci"):                               # varsayılanı olmayan(zorunlu olan) değer sonda olamaz
    print(f"TIK TIK TIK KİM O?\n\t{isim} {soyisim} Geldi Hanım !")

#kimO2()             # isim zorunlu olduğu için hata verir
kimO2("ali")
kimO2("mehmet", "ali")