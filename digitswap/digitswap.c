#include <stdio.h>

int main(){
    int num1, a, b;
    scanf("%d", &num1);
    a = num1/10;
    b = num1%10;
    printf("%d%d", b, a);
    return 0;
}