#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int gs=0,bs=0;
    for(int i=0; i<num; i++){
        int g, b;
        scanf("%d %d", &g, &b);
        gs += g;
        if (gs<b){
            printf("impossible");
            bs=1;
            break;
        }
    }
    if(bs==0){
    printf("possible");    
    }
    return 0;
}