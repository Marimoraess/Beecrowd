#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    for (int c=0;c<n;c++){
        
        float  x,y,resul;
        scanf("%f %f",&x,&y);
        resul=x/y;
        
        if(y==0){
            printf("divisao impossivel\n");
        }
        else{
            printf("%.1f\n",resul);
        }
        
    }

    return 0;
}