#include <stdio.h>
#include <math.h>
#define pi 3.14159265359

int main(){
    int D, V;
    scanf("%d %d", &D, &V);
    while(D+V!=0){
        double d;
        d = (double)pow(pi*pi*(-6*V + pow(D, 3)*pi), (double)1/3)/pi;
        printf("%.9lf\n", d);
        scanf("%d %d", &D, &V);
    }
    return 0;
    
}