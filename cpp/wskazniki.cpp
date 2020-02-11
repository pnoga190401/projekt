/*
 * wskazniki.cpp
 */

#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
    int x = 11;
    cout << "Wartosc x:" << x << endl;
    cout << "Adres x:" << &x << endl;
	cout << "Wartosc pod adresem:" << * &x << endl;
	cout << "Rozmiar x:" << sizeof(x) << endl;
    
    int *px = NULL;
    px = &x;
    cout << "Wartosc wskaznika:" << px << endl;
    cout << "Wartosc pamieci wskazywanej przez wskaznik:" << *px << endl;
    *px = 20;
    cout << *px << endl;
	return 0;
}

