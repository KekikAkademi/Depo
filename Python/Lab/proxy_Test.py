import requests
import pandas as pd 
import json

istek      = requests.get('https://free-proxy-list.net/') 
panda_veri = pd.read_html(istek.text)[0].rename(
    columns={
        'Code'         : 'sil',
        'Anonymity'    : 'sil',
        'Google'       : 'sil',
        'Last Checked' : 'sil'
    }
).drop(columns = 'sil').dropna().reset_index(drop = True)

json_veri = json.loads(panda_veri.to_json(orient='records'))

print(json.dumps(json_veri, indent=2, ensure_ascii=False, sort_keys=False))
