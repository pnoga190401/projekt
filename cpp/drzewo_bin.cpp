/*
 * drzewo_bin.cpp
 */


#include <iostream>
using namespace std;

struct WEZEL {
    int wartosc;
    WEZEL* lewy;
    WEZEL* prawy;
} *korzen = NULL;

WEZEL* stworzWezel(int wartosc) {
    WEZEL* nowyWezel = new WEZEL;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    return nowyWezel;
}

void dodajWezel(WEZEL* wezel, int wartosc) {
    if (korzen == NULL) {
        korzen = stworzWezel(wartosc);
    } else {
        if (wartosc < wezel->wartosc) {
            if (wezel->lewy !=NULL) {
                dodajWezel(wezel->lewy, wartosc);
            } else {
                wezel->lewy = stworzWezel(wartosc);
            }
        } else { // wstawiamy do prawewgo poddrzewa
            if (wezel -> prawy !=NULL) {
                dodajWezel(wezel->prawy, wartosc);
            } else {
                wezel->prawy = stworzWezel(wartosc);
            }
        }
    }
}

void wyswietlRosnaco(WEZEL *wezel) {
    if (wezel !=NULL) {
        wyswietlRosnaco(wezel->lewy);
        cout << wezel->wartosc << ", ";
        wyswietlRosnaco(wezel->prawy);
    }
}

void wyswietlMalejaco(WEZEL *wezel) {
    if (wezel !=NULL) {
        wyswietlMalejaco(wezel->prawy);
        cout << wezel->wartosc << ", ";
        wyswietlMalejaco(wezel->lewy);
    }
}

int main(int argc, char **argv)
{
    dodajWezel(korzen, 8);
    dodajWezel(korzen, 4);
    dodajWezel(korzen, 65);
    dodajWezel(korzen, 23);
    dodajWezel(korzen, 9);
    dodajWezel(korzen, 1);

    cout << "Drzewo niemaleje" << endl;
    wyswietlRosnaco(korzen);
    wyswietlMalejaco(korzen);
	return 0;
}

