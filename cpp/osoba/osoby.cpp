/*
 * osoby.cpp 
 */

#include <iostream>
#include <cstdlib>
#include "osoba.h"

using namespace std;

int main(int argc, char **argv)
{
    bool sukces = false;
	Osoba o1;
    o1.dane();
    Osoba o2("Adam", "Nowak", 34, "M");
    o2.dane();
    sukces = o2.ustawImie("A");
    if (not sukces) {
        cout << "Błąd zmiany imienia" << endl;
    } else {
        o2.dane();
    }
    
    
    sukces = o2.ustawNazwisko("A");
    if (not sukces) {
        cout << "Błąd zmiany nazwiska" << endl;
    } else {
        o2.dane();
    }
    
    
    sukces = o2.ustawWiek(23);
    if (not sukces) {
        cout << "Błąd zmiany wieku" << endl;
    } else {
        o2.dane();
    }
    
    
    sukces = o2.ustawPlec("K");
    if (not sukces) {
        cout << "Błąd zmiany plci" << endl;
    } else {
        o2.dane();
    }
    
	return 0;
}

