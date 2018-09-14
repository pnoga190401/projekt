#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#




def main(args):
    a = a = int(input('Podaj liczbę 1: ')) 
    print(a)
    b = int(input('Podaj liczbę 2: ')) 
    print(b)
    
    if a > b:
        print(a, "jest większe od", b)
    elif a < b:
        print(b, "jest większe od", a)
    else:
        print(a, "jest równe", b)
        
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
