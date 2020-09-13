import os
import subprocess

komut = "iexplore -k http://fakeupdate.net/win10ue/"

#os.startfile(komut)

#os.system(komut)
#os.popen(komut)

def veriTest():
    cmd = "python --version"

    veri = os.system(cmd)
    print('Dönen Veri:', veri)

    veri = os.popen(cmd).read()
    print('Dönen Veri:', veri)

    veri = subprocess.call(cmd, shell=True)
    print('Dönen Veri:', veri)

    veri = subprocess.check_output(cmd).decode("utf-8")
    print('Dönen Veri:', veri)


print()

veri = b"\xff\xfeW\x00i\x00n\x00d\x00o\x00w\x00s\x00d\x00a\x00n\x00 \x00k\x00u\x00r\x00t\x00u\x00l\x00 \x00b\x00i\x00r\x00 \x00a\x00n\x00 \x00\xf6\x00n\x00c\x00e\x00 \x00.\x00.\x00.\x00".decode("utf16")
print(veri)

for i in veri.splitlines():
    print(f"\t{i}")

print()
metin = "Merhaba Dünya"
print(metin.splitlines())

for i in metin.splitlines():
    sifre = i.encode("utf16")
    print(f"\t{sifre}")

print(sifre.decode("utf16"))

print(subprocess.check_output("python --version").decode("utf-8"))


import cv2                              # pip install opencv-python
camera = cv2.VideoCapture(0)            # Video başlat
return_value,image = camera.read()      # İlk fotğrafı al
cv2.imwrite('test.jpg',image)           # Kaydet
camera.release()
cv2.destroyAllWindows()                 # Tüm ekranları kapat