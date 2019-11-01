#include <stdio.h>

typedef struct Binario
{
    int teste : 4;
} Binario;

int main()
{
    Binario teste;
    teste.teste = 10;

    printf("%d\n", teste.teste);
    return 0;
}