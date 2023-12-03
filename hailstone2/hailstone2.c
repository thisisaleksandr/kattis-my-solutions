#include <stdio.h>

int main(){
    long long int num;
    int len=1;
    scanf("%lld", &num);
    while(num!=1){
        if((num%10)%2==1){
            num = 3*num + 1;
        }else{
            num = num/2;
        }
        len++;
    }
    printf("%d", len);
    
    return 0;
}