#include <stdio.h>

int main() {
    char nome[50];
    double A,B,resul;

    scanf("%s", nome);   
    scanf("%lf", &A);
    scanf("%lf",&B);
    
    resul=A+(B*0.15);


    printf("TOTAL = R$ %.2lf\n", resul);

    return 0;
}
