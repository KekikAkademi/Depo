while True:
    cumle = input("Herhangi bir cümle giriniz. : ")

    if cumle:
        if cumle == "q":
            print("Çıktım Babuş")
            break
        else:
            parcala = cumle.split()
            parcala.sort()

            for i in parcala:
                print(i)
    else:
        print("lütfen cümle giriniz.")