/*
 * potega.cpp 
 */


#include <iostream>
using namespace std;

int potega_re(int a, int n){
    if (n == 0)
    return 1;
    return potega_re(a, n-1) * a;
}



int potega_it(int a, int n)
{
    int wynik = 1;
    for(int i = 0; i < n; i++)
        wynik = wynik * a;
        
    return wynik;
        
}



int main(int argc, char **argv)
{
	int a, n;
    cout << "Podaj podstawe i wykladnik";
    cin >> a >> n;
    cout << "Potega" << potega_it(a ,n );
    cout << "Potega" << potega_re(a ,n );
    
	return 0;
}

