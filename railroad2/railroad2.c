#include <stdio.h>

int main(){
    int x, y, z;
    scanf("%d %d", &x, &y);
    z=(x*4-y)%2;
    if(z==1 || z==-1){
        printf("impossible");
    }else{
        printf("possible");
    }
    
    return 0;
}