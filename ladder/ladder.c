#include <stdio.h>
#include <math.h>

int main(){
    int a, b;
    int hyp;
    scanf("%d %d", &a, &b);
    hyp = a/sin(b*3.1415926/180);
    printf("%d", hyp+1);
    
    
    return 0;
}