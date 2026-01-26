#include <stdio.h>

int main()
{
    int x;
    scanf("%d",&x);
    for (int c=1;c<=x;c++){
        if (c%2!=0){
            printf("%d\n",c);
        }
    }

    return 0;
}

