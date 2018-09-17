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
    nazwa_bazy = 'customers'
    con = sqlite3.connect('customers.db')  # polaczenie z baza
    cur = con.cursor()  # utworzenie kursora

# utworzenie tabeli w bazie
    with open('customers.sql', 'r') as plik:
        cur.executescript(plik.read())


# dodawanie danych do bazy
    dane = dane_z_pliku('dane_customers.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO customers VALUES(?, ?, ?)', dane)
    
# dodawanie danych do bazy
    dane = dane_z_pliku('dane_orders.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO orders VALUES(?, ?, ?, ?)', dane)
    
# dodawanie danych do bazy
    dane = dane_z_pliku('dane_subscriptions.txt')
    print(dane)
    dane.pop(0)  # usuniecie piewszego elementu listy (wiersza)
    cur.executemany('INSERT INTO subscriptions VALUES(?, ?, ?, ?)', dane)


    con.commit()  # zatwierdzenie wszystkich operacji w bazie
    con.close() #zamknietcie polaczenia z baza
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
