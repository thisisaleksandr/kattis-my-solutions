#include <stdio.h>

int main(){
    int f=1;
    while (f==1){
        int a, b;
        scanf("%d %d", &a, &b);
        if (a==0 && b==0){
            f=0;
            break;
        }
        int num, mod;
        mod = a%b;
        num = a/b;
        printf("%d %d / %d\n", num, mod, b);
    }
    return 0;
}