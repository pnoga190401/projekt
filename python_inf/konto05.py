#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa02.py
#

class KontoBasic():
    def __init__(self, ile=0, dane={}):
        self.bilans = ile
        self.osoba = dane


    def wplata(self, ile):
        self.bilans += int(ile)
        return self.bilans

    def wyplata(self, ile):
        self.bilans -= int(ile)
        return self.bilans

    def getDone(self, k):
        return self.osoba[k]

    def drukujBilans(self):
        print(self.bilans)


k1 = KontoBasic(100, {'imie': 'Adam', 'nazwisko': 'Nowak'})
k2 = KontoBasic(5000, {'imie': 'Ala', 'nazwisko': 'Kowalska'})

k1.wplata(100)
k2.wplata(1000)
k1.wyplata(500)
k2.wyplata(300)
print(k1.getDone('imie'))
k1.drukujBilans()


class KontoPremium(KontoBasic):
    def __init__(self, ile, dane=(), debet=0):
        Konto.__init__(self, ile, dane) #wywolanie konstruktora rodzica
        self.debet = debet

    def wyplata(self, ile):
        if self.bilans - ile < self.debet:
            print('Brak srodkow')
            return self.bilans
        else:
            return Konto.wyplata(self, ile)
