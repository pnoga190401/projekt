#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# obliczanie potegi liczby naturalnej

def potega_it(a, n):
    
    wynik = 1
    for i in range(n):
        wynik = wynik * a
       # print(wynik)
    return wynik

def main(args):
    
    a, n = 3, 4  # wielokrotne przypisanie 
    print("Podstawa {} do potęgi {} wynosi {}".
           format(a, n, potega_it(a, n)))
    potega_it(a, n) #wywolanie funkcji
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
