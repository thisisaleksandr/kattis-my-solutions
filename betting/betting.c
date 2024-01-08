#include <stdio.h>

int main() {
    int num;
    float num2, num3;
    scanf("%d", &num);
    num2 = (float)100/num;
    num3 = (float)100/(100-num);
    printf("%f\n%f", num2, num3);
}