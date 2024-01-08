#include <stdio.h>
#include <math.h>

int main(){
    int a, b, c, d;
    float s, res;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    s = (float)(a+b+c+d)/2;
    //printf("%f\n", s);
    res = pow(((s-a)*(s-b)*(s-c)*(s-d)), 0.5);
    printf("%f", res);
    
    return 0;
}