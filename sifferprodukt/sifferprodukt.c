#include <stdio.h>

int func(int x){
    int k, counter=1;
    while (x!=0){
        k = x%10;
        if (k!=0){
            counter*=k;
        }
        x = x/10;
    }
    return counter;
}

int main(){
    int num, k, counter=1, zhopa;
    scanf("%d", &num);
    zhopa = num;
    while(zhopa/10!=0){
        zhopa = func(zhopa);
    }
    printf("%d", zhopa);
    return 0;
}