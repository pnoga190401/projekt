/*
 * szyfr_cezara.cpp 
 */

using namespace std;

#include <iostream>
#include <string.h>


void deszyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0'){
    }
}

void szyfruj(char tb[], int klucz){
    int ile = strlen(tb)
    ile znaków uzupelnic kropkami
    uzupelnic kropkami
}

int main(int argc, char **argv)
{
	
    int klucz = 0;
    
    cout << "Podaj tekst w małych literach: " << endl;
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    //szyfruj(tekst, klucz);
    deszyfruj(tekst, klucz);
	return 0;
}
