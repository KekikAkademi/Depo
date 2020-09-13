# /usr/bin/python3.4
# -*- coding: utf-8 -*-
__author__ = 'Mertcan Gökgöz'

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def DolarParse():
    pasteURL = "http://tr.investing.com/currencies/usd-try"
    data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data, 'lxml')
    for dolar in parse.find_all('span', id="last_last"):
        print(f"Güncel Dolar Kuru: {dolar.text}")


def EuroParse():
    pasteURL = "http://tr.investing.com/currencies/eur-try"
    data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data, 'lxml')
    for euro in parse.find_all('span', id="last_last"):
        print(f"Güncel Euro Kuru: {euro.text}")


DolarParse()
EuroParse()