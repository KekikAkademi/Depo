#include <stdio.h>

int main(){
    int tamSayi = 6;
    float ondalikSayi = 3.5;
    double uzunKesir = 5.78549;
    char harf = 'C';

    printf("\nint şudur : %d        \n\t\t-- Bellek : %ld", tamSayi, sizeof(tamSayi));
    printf("\nfloat şudur : %f      \n\t\t-- Bellek : %ld", ondalikSayi, sizeof(ondalikSayi));
    printf("\ndouble şudur : %lf    \n\t\t-- Bellek : %ld", uzunKesir, sizeof(uzunKesir));
    printf("\nchar Şudur : %c       \n\t\t-- Bellek : %ld", harf, sizeof(harf));
    printf("\n");

        /*
        int     > tamsayı       {decimal}   (4 Byte)
        float   > kesirli       {float}     (4 Byte)
        double  > uzunKesir     {longfloat} (8 Byte)
        char    > harf          {char}      (1 Byte)
        */

    return 0;
}