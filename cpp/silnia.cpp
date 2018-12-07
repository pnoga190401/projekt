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

// silnia _re(5)
// silnia_re(4)*5
// silnia_re(3)*4
// silnia_re(2)*3
// silnia_re(1)*2
// silnia_re(0)*1
// 1
// 1 * 1
// 1 * 2
// 2 * 3
// 6 * 4
// 24 * 5
// 120

int main(int argc, char **argv)
{
    int a;
    cout << "Podaj liczbe: ";
    cin >> a;
    cout << "silnia: " << silnia_it(a) << endl;
    cout << "silnia: " << silnia_re(a) << endl;
    
	return 0;
}

