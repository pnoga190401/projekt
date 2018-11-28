/*
 * noga_lpierwsza.cpp
 */


#include <iostream>
#include <cstdlib>

using namespace std;

bool pierwsza(int n){
    if (n < 2)
        return false;
    fot(int i = 2; i * i <= n; i++)
        if(n%i == 0)
            return false;
    return true;
}


int main(int argc, char **argv)
{
	int n;
    cout << "Podaj liczbę naturalną: ";
    cin >> n;
    
    if(pierwsza(n))
        cout << "Liczba " << n << "jest pierwsza" << endl;
    else{ 
        cout << "Liczba " << n << "nie jest pierwsza" << endl;
    }
    
	return 0;
}

