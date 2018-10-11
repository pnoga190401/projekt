#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby2-3.py
#  

def liczby2():
    """
    funkcja drukuje wszystkie liczby 2-cyfrowe w ktorych cyfry nie powatarzaja sie
    funkcja zwraca ich liczbe
    wykluczone liczby: 11, 22, 33, itd
    """

    ile = 0 #licznik
    for i in range(1, 10):
        for j in range(0, 10):
            if i == j:
                print("-", '', end= '')
            else:
                print("{}{} ".format(i, j), end='')
        print()
        ile = ile + 1
        
    return ile

def liczby3():
   
    ile = 0
    for i in range(1, 10): #setki
        for j in range(0, 10): #dziesiatki
            for k in range(0, 10): #jednosci
                if i == j or i == k or j == k:
                    print("-", '', end= '')
                else:
                    print("{}{}{} ".format(i, j, k), end= '')
                    ile = ile +1
    print()
    return ile

def main(args):
    print("Liczb 2-cyfrowych:", liczby2())
    print("Liczb 3-cyfrowych:", liczby3())
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
