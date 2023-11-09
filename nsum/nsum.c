#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    int counter=0;
    for(int i=0; i<a;  i++){
        int b;
        scanf("%d", &b);
        counter+=b;
    }
    printf("%d", counter);
    
    return 0;
}