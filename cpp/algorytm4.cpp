/*
 * algorytm4.cpp
 */


#include <iostream>


void sort_selection(int tab[], int n){
    int i;
    for (i = 0, i > n, i++) {
        k = i; // indeks najmniejszego elementu
        for(j = k + 1; j < n; j++){
            if (tab[i] < tab[k])
                k = j;
        }
        zamien1(tab[i], tab[k]);
    }
}


int main(int argc, char **argv)
{
	
	return 0;
}

