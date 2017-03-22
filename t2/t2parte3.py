#!/usr/bin/env python3
from lxml import html, etree
import requests
import string

def isHex2d(c):
    # Filtra caracteres indesejados
    return len(c)==2 and (c[0] in string.hexdigits and
            c[1] in string.hexdigits)

def main():
   url = 'http://desafio-paradigmas.appspot.com'
   page = requests.get(url)
   tree = html.fromstring(page.content)
   content = tree.xpath("//comment()")
   # Array de hexadecimais está na terceira linha do comentário
   hexstring = content[0].text.split('\n')[2]
   # Decodifica e imprime a string
   print(''.join([bytes.fromhex(c).decode('utf-8') for c in
         hexstring.split(' ') if isHex2d(c)]))


if __name__ == '__main__':
   main()



