#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')  # /t zapisanie tab
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]
            dane.append(rekord)
    return dane


def main(args):
    nazwa_bazy = 'szkola2'
    con = sqlite3.connect('szkola2.db')  # polaczenie z baza
    cur = con.cursor()  # utworzenie kursora

# utworzenie tabeli w bazie
    with open('szkola2.sql', 'r') as plik:
        cur.executescript(plik.read())


# dodawanie danych do bazy
    dane = dane_z_pliku('oceny.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO oceny VALUES(?, ?, ?, ?)', dane)
    
# dodawanie danych do bazy
    dane = dane_z_pliku('przedmioty.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO przedmioty VALUES(?, ?, ?, ?)', dane)
    
# dodawanie danych do bazy
    dane = dane_z_pliku('uczniowie.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO uczniowie VALUES(?, ?, ?, ?)', dane)


    con.commit()  # zatwierdzenie wszystkich operacji w bazie
    con.close() #zamknietcie polaczenia z baza
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
