#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int savedT = 0;
    double savedV=0;
    double counter = 0;
    scanf("%d %lf", &savedT, &savedV);
    for(int i=1; i<num; i++){
        int a;
        double b;
        scanf("%d %lf", &a, &b);
        counter += (double)((double)((savedV+b)/2)*(a-savedT))/1000;
        savedT = a;
        savedV = b;
    }
    printf("%lf", counter);
}