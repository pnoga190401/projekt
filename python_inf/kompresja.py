#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py



def main(args):
    Vk = 74171
    Vnk = 117760
    Vk = input('Dane skompresowane (bajty): ')
    Vnk = input('Dane nieskompresowane (bajty): ')
    Rc = int(Vk) / int(Vnk)* 100
    Rc2 = (1 - int(Vk) / int(Vnk))* 100
    
    Vk = 74171
    Vnk = 117760
    Vk = input('Dane skompresowane (bajty): ')
    Vnk = input('Dane nieskompresowane (bajty): ')
    Rc = int(Vk) / int(Vnk)* 100
    Rc2 = (1 - int(Vk) / int(Vnk))* 100
    
    print('Wspolczynnik kompresji: ', Rc)
    print('Ile miejsca zaoszczedzono : ', Rc2)
    return 0
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
