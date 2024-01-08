#include <stdio.h>

int s=11000, b=1000, x;
void func(int s, int b, int num){
    for(int i=1; i<num/s; i++){
        if(s*i+b*i==num || s*i+b*(i+1) == num){
            printf("%d,%d\n", b, s);
            break;
        }
    }
}

void same(int n, int x){
    if(x%n==0){
        printf("%d,%d\n", n, n);
    }
}

int main(){
    int num, flag;
    scanf("%d", &num);
    printf("%d:\n", num);
    for(int i = 1; i < (num+1)/2; i++){
        func(i, i+1, num);
        same(i+1, num);
    }
    return 0;
}