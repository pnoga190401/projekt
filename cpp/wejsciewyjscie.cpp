/*
 * szablon.cpp
 */


#include <iostream>

using namespace std;

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

    cout << "Suma: " << a + b << endl;
    cout << "Różnica: " << a - b << endl;
    cout << "Iloczyn: " << a * b << endl;
    cout << "Iloraz: " << a / b << endl;
		


	return 0;
}
