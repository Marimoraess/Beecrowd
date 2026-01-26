#include <stdio.h>

int main()
{
    while (1){
       int n;
       scanf("%d",&n);
       if (n==0){
           break;
       }
       int contA=0,contB=0;
       for ( int c=0;c<n;c++){
           int a,b;
           scanf("%d %d",&a,&b);
           
           if (a>b){
               contA++;
           }
           else if(a<b){
               contB++;
           }
           
           
           
       }
       printf("%d %d\n",contA,contB);
    }

    return 0;
}