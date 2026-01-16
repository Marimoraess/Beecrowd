

#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    int x[n];
    for ( int c=0;c<n;c++){
        scanf("%d",&x[c]);
        
    }
    int menor= x[0];
    int posicao =0;
    for (int c=1;c<n;c++){
        if (x[c]<menor){
            menor=x[c];
            posicao=c;
        }
    }
    
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n",posicao);
    
    
        


   

    return 0;
}