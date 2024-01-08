#include <stdio.h>

int main(){
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    if(c<=a-2 && d<=b-2){
        printf("1");
    }else{
        printf("0");
    }
    return 0;
}