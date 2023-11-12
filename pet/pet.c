#include <stdio.h>

int main(){
    int max1=0;
    int max2=0;
    for(int i=1; i<=5; i++){
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        
        if (a+b+c+d > max2){
            max1 = i;
            max2 = a+b+c+d;
        }
    }
    printf("%d %d", max1, max2);
    
    return 0;
}