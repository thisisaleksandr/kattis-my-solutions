#include <stdio.h>
int main(){
    int w, n, counter=0;
    scanf("%d %d", &w, &n);
    for(int i=0; i<n; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        counter += a*b;
    }
    printf("%d", counter/w);
    
    return 0;
}