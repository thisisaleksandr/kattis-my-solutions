#include <stdio.h>

int main(){
    int a, b, counter=0;
    scanf("%d %d", &a, &b);
    for(int i=0; i<b; i++){
        int c;
        scanf("%d", &c);
        counter += c;
        
    }
    int z;
    z = a-b;
    printf("%.4f %.4f", (float)(z*(-3)+counter)/a, ((float)z*3+counter)/a);
    
    return 0;
}