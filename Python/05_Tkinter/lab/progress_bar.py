# pip install tqdm

from tqdm import tqdm
from time import sleep
from random import uniform

for i in tqdm(range(10)):
    sleep(0.2)
    
pbar = tqdm(["a","b","c","d","e","f","g","h","j","k"])
for i in pbar:
    pbar.set_description(f'Processing >> {i}')
    sleep(0.3)
    
for i in tqdm(range(1000), unit=" keystrokes", desc="Loading ", position=1):
    sleep(uniform(0.001, 0.03))