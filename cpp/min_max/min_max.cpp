#include <iostream>
#include <cstdlib>

using namespace std;
void minmax1() {
    char dalej = 't';
    int liczba = 0;
    int min, max;
    cout << "podaj liczbe :";
    cin >> liczba;
    min = max = liczba;
    while (dalej == 't') {
        cout << "podaj liczbe :";
        cin >> liczba;
        if (liczba < min)
            min = liczba;
        if (liczba > max)
            max = liczba;
        cout << "Nastepna? ";
        cin >> dalej;
    }
    cout << "Najmniejsza: " << min << endl;
    cout << "Najwieksza: " << max << endl;
}

void wypelnij(int tab[], int roz) {
    cout << "Podaj " << roz << " liczb: " << endl;
    for (int i=0; i < roz; i++) {
        cin >> tab[i];
    }
}

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL)); //inicjacja generatora liczb pseudolosowych
    for (int i=0; i < roz; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int roz) {
    for (int i=0; i < roz; i++) {
        cout << tab[i] << " ";
    }
}

int min(int tab[], int rozmiar) {
        int min = tab[0]; 
        for(int i = 1; i < rozmiar; i++) {
            if (tab[i] < min)
                min = tab[i];
        }
        return min;
}

int max(int tab[], int rozmiar) {
        int max = tab[0]; 
        for(int i = 1; i < rozmiar; i++) {
            if (tab[i] > max)
                max = tab[i];
        }
        return max;
}

int main()
{
    int rozmiar = 50;
    int tab[rozmiar];
    wypelnij_los(tab, rozmiar);
    drukuj(tab, rozmiar);
    cout << "\n\nMin: " << min(tab, rozmiar) << endl;
    cout << "\n\nMax: " << max(tab, rozmiar) << endl;
    //minmax1();
    return 0;
}
