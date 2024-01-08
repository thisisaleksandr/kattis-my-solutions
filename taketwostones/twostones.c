#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    if (num%2==1){
        printf("Alice");
    }else{
        printf("Bob");
    }
    return 0;
}