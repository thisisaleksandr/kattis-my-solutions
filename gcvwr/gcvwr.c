#include <stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int counter = 0;
    for (int i = 0; i<c; i++){
        int d;
        scanf("%d", &d);
        counter+=d;
    }
    printf("%.f", (a-b)*0.9-counter);
    
    return 0;
}