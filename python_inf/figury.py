#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  
#program drukuje wypelniony prostokat o bokach podanych przez uzytkwnika za pomoca podanego znaku


# 

def prostokat2(a, b, znak):
#pusty prostokat
    a = int(input("Podaj długość boku 1: ")) 
    b = int(input("Podaj długość boku 2: ")) 
    znak = (str(input("Podaj znak: "))
    
    
    
    for i in range(a): #petla zewnetrzna
        for j in range(b): #petla wewnetrzna
            if j == 0 or j == b - 1:
                print(znak, end= '')
            else:
                print(" ", end='')
        print() #znak konca linii, przejscie do nastepnego wiersza


def main(args):
#wypelniony prostokat
    a = int(input("Podaj długość boku 1: ")) 
    b = int(input("Podaj długość boku 2: ")) 
    znak = (str(input("Podaj znak: "))
    
   
    
    for i in range(a):
        for j in range(b):
            print(znak, end= '')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
