import sys, subprocess, os

c_kodu = r'''
#include <stdio.h>

int main(){
    printf("Merhaba C from Python\n");
}
'''

if not os.path.exists('kekik'): 
    with open('kekik.c', 'w') as yaz:
        yaz.write(c_kodu)

    try:            
        subprocess.check_call(["gcc", "kekik.c", "-okekik", "-std=c99", '-w', '-Ofast']) 
    except subprocess.CalledProcessError:
        print("\nMuhtemel syntax hatası..")
        sys.exit()
    except OSError:
        print("gcc yüklü değil veya derlenecek dosya oluşmadı")
        sys.exit()

    c_cikti = subprocess.check_output("./kekik", stderr=subprocess.STDOUT).decode()

    os.remove("kekik")
    os.remove("kekik.c")

    print(c_cikti * 5)
