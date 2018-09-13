#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

# zasieg zmiennych moze byc lokalny lub globalny

def dodaj(a, b):
    return a +b
    
def odejmij(a, b):
    return a -b
    
def pomnoz(a, b):
    return a *b
    
def podziel(a, b):
    return a /b

def main(args):
    # a = 0  # inicjacja zmiennej
    a = int(input('Podaj liczbę 1: ')) 
    print(a)
    b = int(input('Podaj liczbę 2: ')) 
    print(b)
    
    
    
    print("Suma: ", dodaj(a, b))
    print("Różnica: ", odejmij(a, b))
    print("Iloczyn: ", pomnoz(a, b))
    print("Iloraz: ", podziel(a, b))
    
    
    return 0
    
    # duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
