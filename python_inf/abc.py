#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  WARUNKI
#
# program pobiera 3 liczby calkowite i wyswietla liczbe najwieksza

def maks(a, b, c):
    maks = a
    if b > maks:
        maks = b
    elif c > maks:
        maks = c
    return maks



def main(args):
    a = int(input('Podaj liczbę 1: ')) 
    print(a)
    b = int(input('Podaj liczbę 2: ')) 
    print(b)
    c = int(input('Podaj liczbę 3: ')) 
    print(c)
   
    if b <= a >= c:
       print(a, "jest najwieksze")
    elif a<= a >=c:
        print(b, "jest najwiesze")
    else:
        print(c, "jest najwieksze")
        
   
   
   assert(maks(3, 2, 1,) == 3)
   assert(maks(2, 3, 1,) == 3)
   assert(maks(1, 2, 3,) == 3)
   assert(maks(1, 1, 3,) == 3)
   assert(maks(3, 1, 1,) == 3)
   assert(maks(3, 3, 1,) == 3)
   assert(maks(3, 3, 3,) == 3)
        
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
