#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# obliczanie potegi liczby naturalnej

def silnia_it(n):
    """
    n! = 1 * 2 * 3 * ... * n
    """
    
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
       # print(wynik)
    return wynik

def main(args):
    
    n = 3  
    print("{}! silnia wynosi {}".
           format(n, silnia_it(n)))
    silnia_it(n) #wywolanie funkcji
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
