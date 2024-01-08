#include <stdio.h>

int main(){
    int a, b, c, d;
    scanf("%d %d", &a, &b);
    if (b<45){
        c = a - 1;
    }else {
        c = a;
    }
    if (c<0){
        c = 24 + c;
    }
    if (b<45){
        d = 60+b-45;
    }else{
        d = b - 45;
    }
    printf("%d %d", c, d);

    return 0;
}