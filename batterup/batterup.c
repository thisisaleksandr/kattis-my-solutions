#include <stdio.h>

int main(){
    int a, counter=0, c=0;
    scanf("%d", &a);
    for(int i=0; i<a; i++){
        int b;
        scanf("%d", &b);
        if (b>=0 && b<=4){
            counter+=b;
            c++;
        }
    }
    float x;
    x = (float)counter/c;
    printf("%f", x);
    
    return 0;
}