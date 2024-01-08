#include <stdio.h>

int main(){
    
    double engMile;
    scanf("%lf", &engMile);
    printf("%.f", engMile*1000*5280/4854);
    
    return 0;
}