a = "Mahmut"
b = "Ahmet"

print("Bu Binanın Sahibi " + a + " fakat dairenin sahibi " + b)

temp = a            # temp : geçici demek ingiliççede
a = b
b = temp

#a, b = b, a        # ! bu da çalışıyo (python a özel)

print("Bu Binanın Sahibi " + a + " fakat dairenin sahibi " + b)
