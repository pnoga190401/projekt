/*
 * petle.cpp
 */


#include <iostream>
#include <iomanip>

using namespace std;


int zad1() {
    int suma = 0;
    for(int i = 10; i <= 99; i++){
        if (i % 2 == 0)
        suma += suma + i;
    }
    
void zad2() {
   int a, b, c;
   cin >> a;
   cin >> b;
   
   while (a+b!=c){
        a=b;
        b=c;
        cin >>c;
    }
    cout << c;
}



int main(int argc, char **argv)
{
	zad1();
    zad2();
    
	return 0;
}

