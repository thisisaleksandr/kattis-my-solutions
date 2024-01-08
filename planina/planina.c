#include <stdio.h>

int main(){
    int n, counter=4,sq=3, per=2;
    scanf("%d", &n);
    for (int i=1; i<=n; i++){
        counter = sq*sq;
        sq += per;
        per *= 2;
    }
    printf("%d", counter);
    
    return 0;
}