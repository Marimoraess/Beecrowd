#include <stdio.h>
#include <math.h>
int main(){ 
    float num,count=0,media,soma=0;
    for (int c=0;c<6;c++){
        scanf("%f",&num);
        if (num>0){
            count++;
            soma+=num;
            media=soma/count;
        }
        
    }
    printf("%.0f valores positivos\n",count);
    printf("%.1f\n",media);
    return 0;
}
