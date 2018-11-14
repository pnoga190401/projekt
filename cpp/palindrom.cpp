/*
 * palindrom.cpp
 * 
 * 
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char w[], int roz) {
    bool pal = true;
    for(int i = 0; i < roz/2; i++){
        if (w[i] == w[roz -1 - i])
            ;
    }
}

int main(int argc, char **argv)
{
	int roz = 20;
    char wyraz[20];
    cout << "Podaj wyraz: ";
    cin.getline(wyraz, roz);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
    
	return 0;
}

