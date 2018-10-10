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


def main(args):
    print("Liczb 2-cyfrowych:", liczby2())
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
