#include <iostream>
#include <cmath>

void polje_cijelih_brojeva(int niz[]){

    int k = sizeof(niz);

    int i;

    for (i = 0; i < k; i++ ){

        std::cout<<niz[i]<<" ";

    }

    std::cout<<std::endl;

    }

void interval(int niz[],int a, int b){
    int i;

    for ( i = a; i < b; i++){

        std::cout<<niz[i]<<" ";

    }

    std::cout<<std::endl;

    }

void okretanje(int niz[]){

    int k = sizeof(niz);

    float lista[k] = {};

    int i;

    for ( i = 0; i < k ; i++){

        lista[i] = niz[k-i];

    }

    for ( i = 0; i < k; i++){

        niz[i] = lista[i];

    }

    }


void zamjena (int niz [], int a, int b){

    int x = niz[a];

    niz[a] = niz[b];

    niz[b] = x;

}


void sortiranje(int niz []){

    int k = sizeof(niz);

    int i;

    int j;


    for (i = 0; i < k; i++ ){

        std::cout<<niz[i]<<" ";
        
    }
    for(int i=0;i<k-1;i++){

        for(j=i+1; j<k; j++){
            if(niz[ j ] > niz[ i ]){
                  int b=niz[i];
                  niz[i]=niz[j];
                  niz[j]=b;
            }
        }
    }
}

int main(){
    int niz[15] = {11,-7,0,2,5,1,-3,-6,12,8,7,-2,4,6,-1};
    zamjena(niz,4,5);
    okretanje(niz);
    interval(niz,2,13);
    polje_cijelih_brojeva(niz);
    sortiranje(niz);
    return 0;
}