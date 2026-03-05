#include <stdio.h>

int main()
{
    int n,maior,pos;
    
    for (int c=0;c<100;c++){
       
       scanf("%d",&n);
       if(c==0){
           maior=n;
           pos=c;
       }
       else if(n>maior){
           maior=n;
           pos=c;
       }
           
    }
    
    
    printf("%d\n",maior);
    printf("%d\n",pos+1);
    
    

    return 0;
}

