#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
    char nome[50];
    int idade;
    float altura;
} Pessoa;

void ler(Pessoa *pessoas)
{
    FILE *arq;
    int c, cont = 0;
    arq = fopen("pessoas.txt", "r");
    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo.\n");
    }
    else
    {
        while (fscanf(arq, " %s %i %f", pessoas[cont].nome, &pessoas[cont].idade, &pessoas[cont].altura) == 3)
        {
            cont++;
        }
    }
    fclose(arq);
}

int comparar(const void *a, const void *b) {
    const Pessoa *p1 = (const Pessoa *)a;
    const Pessoa *p2 = (const Pessoa *)b;
    return (p1->altura > p2->altura) - (p1->altura < p2->altura);
}

void ordenar(Pessoa *pessoas)
{
    qsort(pessoas, 4, sizeof(Pessoa), comparar);
}

void imprimir(Pessoa *pessoas, int n)
{
    for(int i = 0; i < n; i++)
        {
            printf("%s %i %.1f\n", pessoas[i].nome, pessoas[i].idade, pessoas[i].altura);
        }
}

int main()
{
    int n = 4;
    Pessoa pessoas[n];
    ler(pessoas);
    ordenar(pessoas);
    imprimir(pessoas, n);
    return 0;
}
