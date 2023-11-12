#include <stdio.h>
#include <math.h>

int main(){
    double num, x;
    scanf("%lf", &num);
    x = pow(num, (float)1/num);
    printf("%lf", x);
    
    return 0;
}