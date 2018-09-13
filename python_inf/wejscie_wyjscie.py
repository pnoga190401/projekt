#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

def dodaj():
    print(a +b)

def main(args):
    # a = 0  # inicjacja zmiennej
    a = int(input('Podaj liczbę 1: ')) 
    print(a)
    b = int(input('Podaj liczbę 2: ')) 
    print(b)
    
    dodaj()
    
    print("Suma: ", a + b)
    print("Różnica: ", a - b)
    print("Iloczyn: ", a * b)
    print("Iloraz: ", a / b)
    
    
    return 0
    
    # duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
