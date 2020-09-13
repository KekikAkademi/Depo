mahalle = "ismetpaşa"
print(mahalle)

#print(mahalle[:5])


a = mahalle[:5]         # mahallenin 5. elemanına/indexine kadar    (ismet)
print(a)

b = mahalle[5:]         # mahallenin 5. elemanından sonra           (paşa)
print(b)

print(a + b)            # a ve b 'yi ekrana yazdır                  (ismetpaşa)

c = mahalle[3:6]        # 3. indexten 6.indexe kadar                (etp)
print(c)


#----                   # birleştirme şekilleri***
a = "mehmet"
b = "ali"

print(a + b)
print(a,b)
print("{}{}".format(a,b))
print(f"{a}{b}")