#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#  

def nww(a, b):

     while a != b:  # rozne od 
        if a > b:
            a = a - b
        else:
            b = b - a
      #print(a)
    
     return a


def nwd(a, b):

     while a != b:  # rozne od 
        if a > b:
            a = a - b
        else:
            b = b - a
      #print(a)
    
     return a
    
def main(args):
    a = int(input("Podaj liczbę 1: "))
    b = int(input("Podaj liczbę 2: "))
    print("nwd({}, {}) = {} ". format(a, b, nwd(a, b)))
    print("nww({}, {}) = {} ". format(a, b, nww(a, b)))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
