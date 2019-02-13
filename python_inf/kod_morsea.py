#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kod_morsea.py

kod = {'a': '+-', 'b':'-+++', 'c':'-+-+', 'd':'-++', 'e':'+', 'f':'++-+','g':'--+','h':'++++','i':'++','j':'+---','k':'-+-','l':'+-++','m':'--','n':'-+','o':'---','p':'+--+','q':      '--+-','r':'+-+','s':'+++','t':'-','u':'++-','v':'+++-','w':'+--','x':'-++-','y':'-+--','z':'--++','ą':'+-+-','ć':'-+-++','ę':'++-++','ch':'----','ł':'+-++-','ń':'--+--','ó':      '---+','ś':'+++-+++','ż':'--++-+','ź':'--++-'}

def koduj(tekst)
    for l in tekst:
        print(kod[l])
        
def dekoduj():
    tekst = []
    lit = ' '
        while lit > '':
        lit = input('Podaj kod Morsea:')
        tekst.append(lit)
    print(tekst)
    
def odwrotnie():
    pass

def main(args):
    # ~tekst = input('Podaj tekst: ').lower()
    # ~print("".join([kod[l] for l in tekst]))
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
