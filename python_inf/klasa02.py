#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa02.py
#

bilans = 0

while True:
    print('+ - wplata')
    print('- - wyplata')
    print('0 - koniec')
    op = input ('Dzialanie: ').strip()
    if op== '+':
        ile = input('Wplata :')
        bilans += int(ile)
    elif op == '-':
        ile = input('Wyplata :')
        bilans -= int(ile)
    else:
        break
    print('konto: ', bilans)


print('Konto: ', bilans)
