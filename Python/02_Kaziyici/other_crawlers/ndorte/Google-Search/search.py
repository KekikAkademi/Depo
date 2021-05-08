import requests, random, time, os
from bs4 import BeautifulSoup

class Ara:
    def desktop(self, kelime, hedefsite):
        ua_dir = (os.getcwd() + "/user-agents-desktop.txt")
        with open(ua_dir, "r") as agents:
            agent = random.choice(agents.readlines())
            a = agent.strip()
            header = {
                "User-Agent": str(a)
            }
            agents.close()
        kelimeduzelt = kelime.replace(" ", "+")
        google_url = ("https://www.google.com.tr/search?q="+kelimeduzelt+"&num=100")
        sonuc = requests.get(google_url, headers=header)
        soup = BeautifulSoup(sonuc.text, "html.parser")
        sonuc_blok = soup.find_all('div', attrs={'class': 'g'})
        x = 1
        for i in sonuc_blok:
            cite = i.find('cite')
            cit = str(cite)
            if hedefsite in cit:
                print(hedefsite, str(x), "sırada.")
                break
            else:
                x += 1
    def mobile(self, kelime, hedefsite):
        ua_dir = (os.getcwd() + "/user-agents-mobile.txt")
        with open(ua_dir, "r") as agents:
            agent = random.choice(agents.readlines())
            a = agent.strip()
            header = {
                "User-Agent": str(a)
            }
            agents.close()
        kelimeduzelt = kelime.replace(" ", "+")
        google_url = ("https://www.google.com.tr/search?q="+kelimeduzelt+"&num=100")
        sonuc = requests.get(google_url, headers=header)
        soup = BeautifulSoup(sonuc.text, "html.parser")
        sonuc_block = soup.find_all('span', attrs={'class': 'qzEoUe'})
        x = 1
        for i in sonuc_block:
            link = str(i.text)
            if hedefsite in link:
                print(hedefsite, str(x), "sırada.")
                break

            else:
                x += 1

p = Ara()
p.desktop("kelime", "site")
p.mobile("kelime", "site")


