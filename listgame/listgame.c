#include <stdio.h>

int main(){
    long int num;
    int counter=0, i=2;
    scanf("%ld", &num);
    while(i*i<=num){
        if(num%i==0){
            num=num/i;
            counter++;
            i=2;
        }else{
            i++;
        }
    }
    printf("%d", counter+1);
    
    return 0;
}