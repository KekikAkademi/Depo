import eel

eel.init('www')

@eel.expose
def merhaba_eel():
    print('Eel\'ye Hoş Geldin Yarraam..')

eel.start('index.html')