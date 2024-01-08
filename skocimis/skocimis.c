#include <stdio.h>
#include <stdlib.h>

int main(){
    int a, b, c, x, y;
    scanf("%d %d %d", &a, &b, &c);
    x = b - a - 1;
    y = c - b - 1;
    if (x>y){
        printf("%d", x);
    }else{
        printf("%d", y);
    }
    
    
    return 0;
}