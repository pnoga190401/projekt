/*
 * szablon.cpp
 */


#include <iostream>

using namespace std;

int dodaj(int a, int b)
{
    return a + b;
}
    
int odejmij(int a, int b)
{
    return a - b;
}

int pomnoz(int a, int b)
{
    return a * b;
}

int podziel(int a, int b)
{
    return a / b;
}



int main(int argc, char **argv)
{
	float a, b ;   // deklaracja zmiennej
    a = b = 0;   // inicjacja zmiennej

    cout << "Podaj liczbę 1: ";
    cin >> a;
    cout << a << endl;

    cout << "Podaj liczbę 2: ";
    cin >> b;
    cout << b << endl;

    dodaj(a, b);

    cout << "Suma: " << dodaj(a, b) << endl;
    cout << "Różnica: " << odejmij(a, b) << endl;
    cout << "Iloczyn: " << pomnoz(a, b) << endl;
    cout << "Iloraz: " << podziel(a, b) << endl;
		


	return 0;
}
