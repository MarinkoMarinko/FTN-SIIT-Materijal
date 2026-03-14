#include <stdio.h>

#define MAX 32

unsigned int RUNPP_REG_ERR = 0;

unsigned int setOnes(unsigned int numOnes, unsigned int start);

void printbin(unsigned int x) {
    unsigned int m=0x80000000;
    int s = 0;
    while(m) {
        printf("%s%s", m&x ? "1" : "0", ++s%8 ? "" : " ");
        m >>= 1;
    }
}


int main() {
    unsigned int numOnes, start;
    unsigned int res;

    printf("Unesite broj jedinica: ");
    scanf("%u", &numOnes);
    
    printf("Unesite indeks pocetka niza jedinica: ");
    scanf("%u", &start);

    res = setOnes(numOnes, start);

    printf("Rezultujuci binarni podatak: ");
    printbin(res);
    printf("\n\n");

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n", RUNPP_REG_ERR);
    #endif
    return 0;
}

