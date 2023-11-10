#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i=0; i<num; i++){
        int a, fac=1;
        scanf("%d", &a);
        for(int k=1; k<=a; k++){
            fac *= k;
        }
        printf("%d\n", fac%10);
    }
    return 0;
}