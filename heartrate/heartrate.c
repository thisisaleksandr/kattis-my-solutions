#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for (int i=0; i<num; i++){
        int a;
        float b, c;
        scanf("%d %f", &a, &b);
        c = (float)b/(a-1);
        printf("%.4f ", 60/c);
        printf("%.4f ", (float)60*a/b);
        printf("%.4f\n", (float)60/(b/(a+1)));
    }
    return 0;
}