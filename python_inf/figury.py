#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  
#program drukuje wypelniony prostokat o bokach podanych przez uzytkwnika za pomoca podanego znaku


# 

def trojkat(h, znak)
    h = int(input("Podaj wysokość: "))
    znak = str(input("Podaj znak: "))
    
    for 


def choinka(h, znak):
    h = int(input("Podaj wyskość: ")) 
    znak = str(input("Podaj znak: "))
    
    for i in range(h):
        for j in range(i + 1):
            print(znak, end='')
        print()
    
    return 0
    
def choinka2(h, znak):
    h = int(input("Podaj wyskość: ")) 
    znak = str(input("Podaj znak: "))
    
    for i in range(h):
        for j in range(h - i):
            print(znak, end='')
        print()
    
    return 0

def prostokat(a, b, znak):
#wypelniony prostokat
    a = int(input("Podaj długość boku 1: ")) 
    b = int(input("Podaj długość boku 2: ")) 
    znak = str(input("Podaj znak: "))
    
    
    
    for i in range(a):  #petla zewnetrzna
        for j in range(b):  #petla wewnetrzna
            if j == 0 or j == b - 1:
                print(znak, end= '')
            else:
                print(" ", end='')
        print() #znak konca linii, przejscie do nastepnego wiersza

    return 0

def prostokat2(a, b, znak):
#pusty prostokat
    a = int(input("Podaj długość boku 1: ")) 
    b = int(input("Podaj długość boku 2: ")) 
    znak = str(input("Podaj znak: "))
    
   
    
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(znak, end= '')
            else:
                print(" ", end='')
        print()

    return 0

def main(args):
    h = int(input("Podaj wyskość: ")) 
    znak = str(input("Podaj znak: "))
    
    for i in range(h):
        for j in range(h - i):
            print(znak, end='')
        print()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
