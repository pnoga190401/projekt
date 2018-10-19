/*
 * suma-cyfr.cpp
 */


#include <iostream>
#include <iomanip>

using namespace std;

int sumuj_cyfry1(int a) {
    int suma = 0;
    while (a > 0){
        suma += a % 10;
        a = a / 10;
    }
    return suma;
}

int main(int argc, char **argv)
{
	int a = 0;
   
    while(a < 10) {
        cout << "Podaj liczbe 2cyfrowa: ";
        cin >> a;
    }
    
    cout << "Suma: " << sumuj_cyfry1(a) << endl;
    
	return 0;
}

