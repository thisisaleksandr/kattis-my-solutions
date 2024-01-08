#include <stdio.h>

int main(){
    int n, day=0, printer=1;
    scanf("%d", &n);
    while(printer<n){
        day+=1;
        printer*=2;
    }
    printf("%d", day+1);

    return 0;
}