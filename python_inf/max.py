#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  max.py  
#  


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
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
