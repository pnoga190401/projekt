#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  


 #   JUPYTER-QTCONSOLE


def trojkat(a, b, c):
    """
    funkcja bada mozliwosc zbudowania trojkata z tzrech podanych bokow
    funkcja zwraca True jezeli sie da False w przeciwnym wypadku
    """
    
    if a + b > c and a + c > b and c + b > a:
        return True

    return False
    
def main(args):
    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
    #a = int(input('Podaj bok 1: ')) 
    #b = int(input('Podaj bok 2: ')) 
    #c = int(input('Podaj bok 3: ')) 
    
    # if trojkat(a, b, c):
        # print("Da się")
    # else:
        # print("Nie da się")
    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
