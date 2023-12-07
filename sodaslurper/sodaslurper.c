#include <stdio.h>

int main(){
    int e, f, c, counter=0, newempty =0, rem=0;
    int newbottle;
    scanf("%d %d %d", &e, &f, &c);
    e = e+f;
    while(e>=c){
        counter+=e/c;
        e = (e/c + e%c);
    }
    printf("%d", counter);
    
    return 0;
}