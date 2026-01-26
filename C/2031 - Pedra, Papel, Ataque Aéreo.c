#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int c = 0; c < n; c++) {
        char jog1[50], jog2[50];

        scanf("%s", jog1);
        scanf("%s", jog2);

        if (strcmp(jog1, "ataque") == 0 && strcmp(jog2, "pedra") == 0) {
            printf("Jogador 1 venceu\n");
        }
        else if (strcmp(jog2, "ataque") == 0 && strcmp(jog1, "pedra") == 0) {
            printf("Jogador 2 venceu\n");
        }
        else if (strcmp(jog1, "pedra")==0 && strcmp(jog2, "papel")==0){
            printf("Jogador 1 venceu\n");
        }
        else if (strcmp(jog2, "pedra")==0 && strcmp(jog1, "papel")==0){
            printf("Jogador 2 venceu\n");
        }
        else if (strcmp(jog2, "papel")==0 && strcmp(jog1, "papel")==0){
            printf("Ambos venceram\n");
        }
        else if (strcmp(jog2, "pedra")==0 && strcmp(jog1, "pedra")==0){
            printf("Sem ganhador\n");
        }
        else if (strcmp(jog1, "ataque")==0 && strcmp(jog2, "ataque")==0){
            printf("Aniquilacao mutua\n");
        }
        else if (strcmp(jog1, "ataque")==0 && strcmp(jog2, "papel")==0){
            printf("Jogador 1 venceu\n");
        }
        else if (strcmp(jog2, "ataque")==0 && strcmp(jog1, "papel")==0){
            printf("Jogador 2 venceu\n");
        }
        
        
        
        
        
    }

    return 0;
}
