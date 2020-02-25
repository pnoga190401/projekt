#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa02.py
#

bilans = 0

def utworzKonto(imie):
    return {'kto': imie.lower(), 'bilans': 0}

def wplata(klient):
    ile = input('wplata: ')
    bilans += int(ile)
    return klient

def wyplata(klient):
    ile = input('wplata: ')
    bilans -= int(ile)
    return klient

konta = [utworzKonto('Ala'), utworzKonto('Bela')]

kto = None

while True:
    if not kto:
        kto = input('Imie: ').strip().lower()
        klient = None
        for o in konta:
            if o['kto'] == kto:
                klient = o
        if not klient:
            print('nie ma konta')
            kto = None
            continue
    print('+ - wplata')
    print('- - wyplata')
    print('0 - koniec')
    op = input ('Dzialanie: ').strip()
    if op== '+':
        klient = wplata(klient)
    elif op == '-':
        klient = wyplata(klient)
    else:
        break
    print('konto: ', klient['kto'], ':', konto['bilans'])


print('Konto: ', bilans)
