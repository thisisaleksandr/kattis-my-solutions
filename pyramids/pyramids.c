#include <stdio.h>

int main(){
    int k, n=1, c=0;
    scanf("%d", &k);
    while (k>=n*n){
        c++;
        k = k-n*n;
        n+=2;
    }
    printf("%d", c);
    
    return 0;
}