/*
 * fibonacci.cpp
 */


#include <iostream>

using namespace std;

long int fibonacci_it(int n) {
    long int a = 0;  // wyraz n-2
    long int b = 1;  // wyraz n-1
    
        if(n == a) return a;
        else if (n == b) return b;
        
        int wynik = 0;
        for(int i = 2; i <= n; i++){
            wynik = a + b;
            a = b;
            b = wynik;
            
        }
        return wynik;
    
    
}


int main(int argc, char **argv)
{
	int n =0;
    cout << "Podaj numer wyrazu ciagu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ";" << endl;
    for (int i = 0; i <= n; i++){
        cout << fibonacci_it(i) << endl;
    }
    cout << fibonacci_it(n);
    
    
	return 0;
}

