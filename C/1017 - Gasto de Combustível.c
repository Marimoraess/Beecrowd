#include <stdio.h>

int main(){
    
    int gastHo,kmH;
    float li,kmL;
    scanf("%d",&gastHo);
    scanf("%d",&kmH);
    
    kmL= gastHo*kmH;
    li=kmL/12;
    
    
    printf("%.3f\n",li);
    
    return 0;
}