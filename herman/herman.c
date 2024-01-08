#include <stdio.h>

int main(){
    int num;
    double taxi, ev;
    scanf("%d", &num);
    ev = 3.14159265359 * num * num;
    taxi = num*num*2;
    printf("%lf\n%lf", ev, taxi);
    
    
    return 0;
}