a = "Mahmut"
b = "Ahmet"

print("Bu Binanın Sahibi " + a + " fakat dairenin sahibi " + b)

a, b = b, a

#a, b = b, a        # ! bu da çalışıyo (python a özel)

print("Bu Binanın Sahibi " + a + " fakat dairenin sahibi " + b)
