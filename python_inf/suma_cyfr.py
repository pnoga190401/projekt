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

def suma2(liczba):
    suma = 0
    for cyfra in str(liczba):
        suma += int(cyfra)
        
    return suma
        
def main(args):
    liczba = int(input('Podaj liczbę 2-cyfrowa: ')) 
    
    while liczba < 10:
        liczba = int(input('Błędny zakres! Podaj liczbę 2-cyfrowa: '))
        
    
    print("Suma: ", suma2(liczba))
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
