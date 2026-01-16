#include <stdio.h>
#include <math.h>
int main(){
    int n,nAno,nMes,nDias;
    scanf("%d",&n);
    nAno=n/365;
    n=n%365;
    
    nMes=n/30;
    nDias=n%30;
    
    printf("%d ano(s)\n",nAno);
    printf("%d mes(es)\n",nMes);
    printf("%d dia(s)\n",nDias);
    return 0;
}