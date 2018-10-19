/*
 * euklides.cpp
 */


#include <iostream>
#include <iomanip>

using namespace std;





int main(int argc, char **argv)
{
	int a, b;
    cout << "Podaj 2 liczby: ";
    cin >> a >> b;
    inr nwd = nwd1(a, b);
    cout << "NWD (" << a << ","
    << b << ") = "
    << nwd << endl;
    
	return 0;
}

