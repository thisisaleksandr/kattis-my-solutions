#include <stdio.h>

int main(){
    int n, h, v;
    scanf("%d %d %d", &n, &h, &v);
    if (n-h > n/2){
        if (n-v>n/2){
            printf("%d",4*(n-v)*(n-h));
        }else {
            printf("%d", 4*(n-h)*v);
        }
    }else{
        if (n-v>n/2){
            printf("%d",4*(n-v)*h);
        }else {
            printf("%d", 4*h*v);
        }        
    }

    return 0;
}