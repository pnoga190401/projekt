#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfry.py
#  

def suma1(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
        
    return suma
        
def main(args):
    liczba = int(input('Podaj liczbę 2-cyfrowa: ')) 
    liczba = int(liczba) 
    
    while liczba < 10:
        liczba = int(input('Błędny zakres! Podaj liczbę 2-cyfrowa: '))
        liczba = int(liczba)
    
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
    print("Suma: ", suma1(liczba))
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
