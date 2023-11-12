#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    if(4*b*b>=2*a*a){
        printf("fits");
    }else{
        printf("nope");
    }
    
    return 0;
}