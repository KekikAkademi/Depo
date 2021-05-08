import socket

ipListesi = ["194.145.216.81","89.80.180.37"]
portListesi = []
bannerListesi = []

for ip in ipListesi:
    print(f"\n\n\t\t[~] Taranan IP : {ip}\n")
    for port in range(20,26):
        try:
            soket = socket.socket()
            soket.connect((ip, port))
            banner = soket.recv(1024).decode("utf-8").strip()

            print(f"[+] Açık Port : {port} | {banner}")
            portListesi.append(port)
            bannerListesi.append(banner)

            if port == 22:
                print("\t[!] Sistem Linux veya Network Cihazı Olabilir!")
                with open("linux.txt", "a", encoding="utf-8") as linuxDosya: linuxDosya.write(f"{ip}\n")
            elif port == 135 or port == 137 or port == 445:
                print("\t[!] Sistem Windows Olabilir!")
                with open("windows.txt", "a", encoding="utf-8") as windowsDosya: windowsDosya.write(f"{ip}\n")

            with open(f"{banner.replace(' ','_')}.txt", "a", encoding="utf-8") as bannerDosya: bannerDosya.write(f"{ip}\n")


            print("=" * 75)
            soket.close()
        except:
            pass

print(portListesi)
print(bannerListesi)