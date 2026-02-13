#include <stdio.h>

int main()
{
    int p, j1, j2, soma, r, a;
    scanf("%d %d %d %d %d", &p, &j1, &j2, &r, &a);

    soma = j1 + j2;

    // 1°
    if (soma % 2 == 0 && p == 1 && r == 1 && a == 1){
        printf("Jogador 2 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 1 && r == 1 && a == 1){
        printf("Jogador 2 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 0 && r == 1 && a == 1){
        printf("Jogador 2 ganha!\n");
    }
    else if (soma % 2 == 0 && p == 0 && r == 1 && a == 1){
        printf("Jogador 2 ganha!\n");
    }

    // 2°
    else if (soma % 2 == 0 && p == 1 && r == 0 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 1 && r == 0 && a == 0){
        printf("Jogador 2 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 0 && r == 0 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 == 0 && p == 0 && r == 0 && a == 0){
        printf("Jogador 2 ganha!\n");
    }

    // 3°
    else if (soma % 2 == 0 && p == 1 && r == 1 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 1 && r == 1 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 0 && r == 1 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 == 0 && p == 0 && r == 1 && a == 0){
        printf("Jogador 1 ganha!\n");
    }

    // 4°
    else if (soma % 2 == 0 && p == 1 && r == 0 && a == 1){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 1 && r == 0 && a == 1){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 != 0 && p == 0 && r == 0 && a == 1){
        printf("Jogador 1 ganha!\n");
    }
    else if (soma % 2 == 0 && p == 0 && r == 0 && a == 1){
        printf("Jogador 1 ganha!\n");
    }

    return 0;
}
