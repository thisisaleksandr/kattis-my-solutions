#include <stdio.h>
int harshad(int number){
    int sum = 0;
    while(number!=0){
        sum += number%10;
        number /=10;
    }
    return sum;
}

int main(){
    int num, chislo;
    scanf("%d", &num);
    chislo = 1;
    while (chislo!=0){
        if (num%harshad(num)==0){
            printf("%d", num);
            chislo = 1;
            break;
        }else{
            num++;
        }
    }
    
}