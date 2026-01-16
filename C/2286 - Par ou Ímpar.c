#include <stdio.h>

int main()
{
    int n, teste=1;
    
    scanf("%d",&n);
    while (n!=0){
        
        char jog1[11],jog2[11];
        scanf(" %s",&jog1);
        scanf(" %s",&jog2);
        printf("Teste %d\n",teste);
        for (int c=0; c<n; c++){
            int A,B,soma;
            scanf("%d %d",&A,&B);
            
            soma= A+B;
            if (soma%2==0){
                printf("%s\n",jog1);
            }
            else{
                printf("%s\n",jog2);
            }
        }
        printf("\n");
        teste++;
        scanf("%d",&n);
        
    }

   

    return 0;
}