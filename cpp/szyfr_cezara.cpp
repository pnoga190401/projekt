/*
 * szyfr_cezara.cpp 
 */

using namespace std;

#include <iostream>
#include <string.h>
#define MAKS 100

void szyfruj(char tekst, int klucz){
    for(i = 1; i < MAKS; i++ )
    int kod = 0;
    for (int i = 0; i < roz; i++){
        kod = (int)tb[i];
        if (kod > 96 && kod < 123)
            kod -= 32;
            //cout << (char)(kod-32) << " ";
        else if (kod > 64 && kod < 91)
            kod += 32;
            //cout << (char)(kod+32) << " ";
        //else
            //cout << tb[i] << " ";
        cout << (char)kod << " ";
    }
}

int main(int argc, char **argv)
{
	char tekst[MAKS];
    int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz)
	return 0;
}

