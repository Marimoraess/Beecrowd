
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    for (int c=1;c<=n;c++){
        if (n%c==0){
            printf("%d\n",c);
        }
    }

    return 0;
}