#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_for.py
#  



def main(args):
    liczba = int(input('Podaj liczbę początkowa: ')) 
    liczba2 = int(input('Podaj liczbę końcowa: ')) 
    
    while liczba2 <= liczba:
        liczba2 = int(input('Błędny zakres! Podaj liczbę początkowa: '))
    
    if liczba2 <= liczba:
        print("Błędny zakres")
        exit(0)
        
    for liczba in range(liczba, liczba2 + 1):
        if liczba % 2 == 0:
            print(liczba)
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
