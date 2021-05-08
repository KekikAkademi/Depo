import eel, os, random

eel.init('www')

@eel.expose
def py_dosya_sec(dizin):
    if os.path.isdir(dizin):
        return random.choice(os.listdir(dizin))
    else:
        return 'Geçerli bir dizin değil..'

eel.start('index.html')