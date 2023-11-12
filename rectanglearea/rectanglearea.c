#include <stdio.h>
#include <math.h>

int main(){
    double a, b, c, d, area;
    scanf("%lf %lf %lf %lf", &a, &b, &c, &d);
    area = fabs(c-a) * fabs(d-b);
    printf("%lf", area);
    
    return 0;
}