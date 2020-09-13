# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from colorama import Fore
from time import sleep
import random

renkler = [
    Fore.RED,
    Fore.GREEN,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.YELLOW,
    Fore.CYAN,
    Fore.WHITE,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTYELLOW_EX
]


def kisir():
    for i in range(20):
        print(f'{random.choice(renkler)} Kısır Döngü')
        sleep(0.2)