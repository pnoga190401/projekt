/*
 * znaki.cxx
 */



#include <iostream>
#include <string.h>

using namespace std;

//~void zamiana_liter(char tb[])
//~{   
    //~int i = 0;
    //~int kod = 0;
    //~while(tb[i] != '\0') {
        //~kod = (int)tb[i];
        //~if (kod > 64 && kod < 91)
            //~kod += 32;
        //~else if (kod > 96 && kod < 123)
            //~kod -= 32;
        //~cout << (char)kod;
          
        //~i++;
    //~}
//~}



void licz_znaki(char tb[], int roz) {
    //~for(int i=0; i < roz; i++) {
       //~cout << tb[i];
    //~}
    int i = 0;
    int cyfry, literyD, literyM, reszta;
    cyfry = literyD = literyM = reszta = 0;
    int znak_kod = 0; //kod ASCII badanego znaku
    
    
    while(tb[i] != '\0'){
        znak_kod = (int)tb[i];
        if (znak_kod > 64 && znak_kod < 91) // to sprawia że sa duże litery
            literyD++;
        else if (znak_kod > 96 && znak_kod < 123)
            literyM++;
        else if (znak_kod > 47 && znak_kod < 58)
            cyfry++;
        else 
            reszta++;
        
    i++;  //inkrementcja indeksu
   }
    cout << "Duże litery: " << literyD << endl; 
    cout << "Małe litery: " << literyM << endl; 
    cout << "Cyfry: " << cyfry << endl;
    cout << "Reszta: " << reszta << endl; 
}

int zlicz(char tb[]){
    int i = 0;
    while (tb[i] != '\0') i++;
    return i;
}

void ascii(char tb[], int roz){
    int kod = 0;
    for (int i = 0; i < roz; i++){
        kod = (int)tb[i];
        if (kod > 96 && kod < 123)
            cout << (char)(kod-32) << " ";
        else if (kod > 64 && kod < 91)
            cout << (char)(kod+32) << " ";
        else
            cout << tb[i] << " ";
    }
}

void odwroc(char tb[], int roz){
    for(int i = roz - 1; i >= 0; i--)
        cout << tb[i] <<  " ";
}


int main(int argc, char **argv)
{
    const int rozmiar = 20;
	char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    //licz_znaki(znaki, cin.gcount());
    int ilosc = 0;
    //int ilosc = cin.gcount();
    //ilosc = zlicz(znaki);
    ilosc = strlen(znaki);
    //cout << ilosc;
    ascii(znaki, ilosc);
    //zamiana_liter(znaki);
	return 0;
}

