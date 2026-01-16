
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n!=0){
        int contM=0,contJ=0;
        for (int c=0;c<n;c++){
            int r;
            scanf("%d",&r);
            if (r==0){
                contM++;
            }
            else{
                contJ++;
            }
        }
        printf("Mary won %d times and John won %d times\n",contM,contJ);
        scanf("%d",&n);
    }
    

    return 0;
}