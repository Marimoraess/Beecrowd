#include <stdio.h>

int main()
{
    int q,v,cont1=0,cont0=0;
    scanf("%d",&q);
    for (int c=0;c<q;c++){
        scanf("%d",&v);
        if(v==1){
            cont1++;
    }
        else{
            cont0++;
        }
    }
    
    if(cont0> cont1){
        printf("Y\n");
    }
    else{
        printf("N\n");
    }

    return 0;
}
