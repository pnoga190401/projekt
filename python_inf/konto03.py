#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa02.py
#

bilans = 0

def wplata(bilans):
    ile = input('wplata: ')
    bilans += int(ile)
    return bilans

def wyplata(bilans):
    ile = input('wplata: ')
    bilans -= int(ile)
    return bilans


while True:
    print('+ - wplata')
    print('- - wyplata')
    print('0 - koniec')
    op = input ('Dzialanie: ').strip()
    if op== '+':
        bilans = wplata(bilans)
    elif op == '-':
        bilans = wyplata(bilans)
    else:
        break
    print('konto: ', bilans)


print('Konto: ', bilans)
