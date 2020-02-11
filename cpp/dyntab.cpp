/*
 * dyntab.cpp 
 */


#include <iostream>
using namespace std;

void tabd_1() {
    float *tb = NULL;
    int ile;
    float liczba;
    
    cout << "ile liczb podasz?" << endl;
    cin >> ile;
    
    try {
        tb = new float[ile];
    } catch(bad_alloc) {
        cout << "za malo pamieci!";
        //return -1;
    }
    
    for (int i=0; i<ile; i++) {
        cout << "podaj liczbe:";
        cin >> liczba;
        cout << (tb+i) << endl;
        *(tb+i) = liczba;
    }
    
    delete [] tb; // zwolnienie pameci
}

void tabd_2() {
     int w, k, i, j;
     srand(time(NULL));
     cout << "Podaj liczbe wierszy i kolumn tablicy:";
     cin >> w >> k;
     int **tb; // deklaracja wskznika do wskaznika
     try {
        tb = new int *[w];
    } catch(bad_alloc) {
        cout << "Blad";
    
    }
    
    for (i=0; i<w; i++){
        try {
            tb[i] = new int[k];
            } catch(bad_alloc) {
                cout << "Blad";
            }
    for (i=0; i<w; i++) {
        for (j=0; j<k; j++) {
            tb[i][j] = rand() % 101;
            cout << setw(4) << tb[i][j];
        }
        cout << endl;
    }
    
    for (i=0; i<w; i++) {
        delete [] tb[i];
    }
    delete [] tb;
}

int main(int argc, char **argv) {
    tabd_1();
    tabd_2();
	return 0;
}

