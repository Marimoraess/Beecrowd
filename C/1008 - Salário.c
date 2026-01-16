#include <stdio.h>

int main(){
    int func,horas;
    float porhora,sal;
    
    scanf("%d",&func);
    scanf("%d",&horas);
    scanf("%f",&porhora);
    
    sal=horas*porhora;
    
    printf("NUMBER = %d\n",func);
    printf("SALARY = U$ %.2f\n",sal);
    
    
    
    
    
    return 0;
}