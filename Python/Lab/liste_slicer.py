def liste_parcala(liste:list, adet:int) -> list :
    fark  = len(liste) / float(adet)
    cikti = []
    son   = 0.0

    while son < len(liste):
        cikti.append(liste[int(son):int(son + fark)])
        son += fark

    return cikti

liste = ['bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz', 'on', 'on bir']

print(liste)

print('\n\n\n')

print(liste_parcala(liste, 2))

print('\n\n\n')

print(liste_parcala(liste, 3))

print('\n\n\n')

print(liste_parcala(liste, 4))
