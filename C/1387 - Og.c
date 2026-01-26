#include <stdio.h>

int main()
{
    while (1){
        int l,r,res;
        scanf("%d %d",&l,&r);
        if (l==0 && r==0){
            break;
        }
        res=l+r;
        printf("%d\n",res);
    }

    return 0;
}