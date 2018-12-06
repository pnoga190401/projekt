/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;


int silnia_re(int a){
    if (a == 0)
    return 1;
    return silnia_re(a - 1) * a;
}


int silnia_it(int a){
    int wynik = 1;
    for (int i = 1; i < a + 1; i++){
        wynik = wynik * i;
    }
    return wynik;
}


int main(int argc, char **argv)
{
    int a;
    cout << "Podaj liczbe: ";
    cin >> a;
    cout << "silnia: " << silnia_it(a) << endl;
    cout << "silnia: " << silnia_re(a) << endl;
    
	return 0;
}

