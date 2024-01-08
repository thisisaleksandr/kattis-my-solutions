#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int piece = num;

    if(num%2==0){
        printf("Alice\n%d", 1);
    }else{
        printf("Bob");
    }
}