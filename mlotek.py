#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby
    # print('wylosowano:', liczba)
    # pobieranie danych od uzytkowanika
    for i in range(3):
        print('proba', i + 1)
        odp = input('podaj liczbę od 1 do 10: ')
        print('podałeś liczbę: ', odp)

        if liczba == int(odp):  # porownanie  odp z wylosowana liczba
            print ('zgadłeś')
            break  # przerwaie dzialania petli
        elif i == 2:
            print('wylosowano: ', liczba)
        else:
            print ('spróbuj innym razem')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
